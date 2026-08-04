"""Complete Mendeley authorization-code setup through a loopback callback.

The one-time authorization code and generated access token remain in memory.
Only the refresh token is stored in the configured, git-ignored dotenv file so
later commands can generate short-lived bearer tokens dynamically.
"""

from __future__ import annotations

import argparse
import hmac
import html
import os
import secrets
import sys
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlencode, urlparse

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dotenv import set_key, unset_key  # noqa: E402

from eyedatahub.utils.credentials import load_credentials  # noqa: E402
from hub.audit.inventory_unresolved_quantity_deposits import (  # noqa: E402
    MENDELEY_AUTH_API_ROOT,
    MENDELEY_TOKEN_ENDPOINT,
    _curl_json_request,
)


class _ReusableHTTPServer(HTTPServer):
    allow_reuse_address = True


def _validate_redirect_uri(value: str) -> tuple[str, int, str]:
    parsed = urlparse(value)
    if parsed.scheme != "http" or parsed.hostname not in {
        "localhost",
        "127.0.0.1",
        "::1",
    }:
        raise RuntimeError(
            "MENDELEY_REDIRECT_URI must be an HTTP localhost callback."
        )
    if parsed.query or parsed.fragment or parsed.username or parsed.password:
        raise RuntimeError("MENDELEY_REDIRECT_URI must not contain extra URL fields.")
    if not parsed.port:
        raise RuntimeError("MENDELEY_REDIRECT_URI must include an explicit port.")
    return parsed.hostname, parsed.port, parsed.path or "/"


def _callback_handler(
    *,
    expected_path: str,
    expected_state: str,
    result: dict[str, str | None],
) -> type[BaseHTTPRequestHandler]:
    class CallbackHandler(BaseHTTPRequestHandler):
        def log_message(self, _format: str, *_args: Any) -> None:
            return

        def do_GET(self) -> None:  # noqa: N802 - standard-library callback name
            parsed = urlparse(self.path)
            if parsed.path != expected_path:
                self.send_error(404)
                return
            values = parse_qs(parsed.query)
            returned_state = (values.get("state") or [""])[0]
            code = (values.get("code") or [""])[0]
            error = (values.get("error_description") or values.get("error") or [""])[0]
            if not hmac.compare_digest(returned_state, expected_state):
                result["error"] = "The OAuth callback state did not match."
            elif error:
                result["error"] = f"Mendeley authorization was not granted: {error}"
            elif not code:
                result["error"] = "Mendeley returned no authorization code."
            else:
                result["code"] = code

            succeeded = bool(result.get("code"))
            heading = "Authorization received" if succeeded else "Authorization failed"
            message = (
                "You may close this tab and return to EyeDataHub."
                if succeeded
                else html.escape(str(result.get("error") or "Unknown authorization error"))
            )
            body = (
                "<!doctype html><meta charset='utf-8'>"
                f"<title>{heading}</title><h1>{heading}</h1><p>{message}</p>"
            ).encode("utf-8")
            self.send_response(200 if succeeded else 400)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

    return CallbackHandler


def authorize(*, timeout_seconds: int, authorization_url_file: Path) -> dict[str, Any]:
    env_path = load_credentials(login_huggingface=False)
    if env_path is None:
        raise RuntimeError("No dotenv file was found.")
    client_id = os.environ.get("MENDELEY_CLIENT_ID", "").strip()
    client_secret = os.environ.get("MENDELEY_SECRET", "").strip()
    redirect_uri = os.environ.get("MENDELEY_REDIRECT_URI", "").strip()
    if not client_id or not client_secret or not redirect_uri:
        raise RuntimeError(
            "MENDELEY_CLIENT_ID, MENDELEY_SECRET, and MENDELEY_REDIRECT_URI are required."
        )

    hostname, port, callback_path = _validate_redirect_uri(redirect_uri)
    bind_host = "127.0.0.1" if hostname in {"localhost", "127.0.0.1"} else "::1"
    state = secrets.token_urlsafe(32)
    result: dict[str, str | None] = {"code": None, "error": None}
    handler = _callback_handler(
        expected_path=callback_path,
        expected_state=state,
        result=result,
    )
    server = _ReusableHTTPServer((bind_host, port), handler)
    server.timeout = 1
    authorization_query = urlencode(
        {
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "response_type": "code",
            "scope": "all",
            "state": state,
        }
    )
    authorization_url = (
        f"{MENDELEY_AUTH_API_ROOT}/oauth/authorize?{authorization_query}"
    )
    resolved_url_file = authorization_url_file.resolve()
    allowed_work_root = (ROOT / ".audit-work").resolve()
    if not resolved_url_file.is_relative_to(allowed_work_root):
        raise RuntimeError("The authorization URL file must remain under .audit-work.")
    resolved_url_file.parent.mkdir(parents=True, exist_ok=True)
    resolved_url_file.write_text(authorization_url, encoding="utf-8")

    print("Mendeley authorization callback is ready; opening the browser.", flush=True)
    opened = webbrowser.open_new_tab(authorization_url)
    if not opened and os.name == "nt":
        os.startfile(authorization_url)  # type: ignore[attr-defined]

    deadline = time.monotonic() + timeout_seconds
    try:
        while not result["code"] and not result["error"]:
            if time.monotonic() >= deadline:
                raise TimeoutError("Mendeley authorization timed out.")
            server.handle_request()
    finally:
        server.server_close()
        resolved_url_file.unlink(missing_ok=True)

    if result["error"]:
        raise RuntimeError(str(result["error"]))
    code = str(result["code"] or "")
    status_code, payload = _curl_json_request(
        url=MENDELEY_TOKEN_ENDPOINT,
        method="POST",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        basic_auth=(client_id, client_secret),
        form={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri,
        },
    )
    code = ""
    result["code"] = None
    if status_code >= 400:
        raise RuntimeError(
            f"Mendeley authorization-code exchange returned HTTP {status_code}."
        )
    if not isinstance(payload, dict):
        raise RuntimeError("Mendeley returned an unexpected token response.")
    access_token = str(payload.get("access_token") or "").strip()
    refresh_token = str(payload.get("refresh_token") or "").strip()
    if not access_token or not refresh_token:
        raise RuntimeError("Mendeley returned no access token or refresh token.")

    set_key(str(env_path), "MENDELEY_REFRESH_TOKEN", refresh_token)
    for stale_name in (
        "MENDELEY_TOKEN",
        "MENDELEY_AUTHORIZATION_CODE",
        "MENDELEY_AUTHORIZATION_RESPONSE_URL",
        "MENDELEY_OAUTH_STATE",
    ):
        if os.environ.get(stale_name) is not None:
            unset_key(str(env_path), stale_name)
    expires_in = payload.get("expires_in")
    access_token = ""
    refresh_token = ""
    return {
        "authorization_completed": True,
        "refresh_token_stored_in_dotenv": True,
        "access_token_stored": False,
        "expires_in": int(expires_in) if isinstance(expires_in, (int, float)) else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeout-seconds", type=int, default=300)
    parser.add_argument(
        "--authorization-url-file",
        type=Path,
        default=ROOT / ".audit-work" / "mendeley-authorization-url.txt",
    )
    args = parser.parse_args()
    outcome = authorize(
        timeout_seconds=args.timeout_seconds,
        authorization_url_file=args.authorization_url_file,
    )
    print(
        "Mendeley authorization completed; the refresh token is stored in .env "
        f"and the access token lifetime is {outcome['expires_in']} seconds."
    )


if __name__ == "__main__":
    main()
