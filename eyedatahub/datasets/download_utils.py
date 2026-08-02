"""Dataset download utilities for EyeDataHub."""
from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
import tarfile
import urllib.error
import urllib.request
import zipfile
from pathlib import Path
from typing import List, Optional
from urllib.parse import quote

import requests
from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)


def _load_dotenv() -> None:
    """Re-run credential loading (no-op if already done at import time)."""
    from eyedatahub.utils.credentials import load_credentials
    load_credentials()

console = Console()

CHUNK_SIZE = 1024 * 1024  # 1 MiB
DOWNLOAD_ATTEMPTS = 3


def _response_total(headers: object, completed: int) -> int:
    """Return the full transfer size when response headers expose it."""
    content_range = headers.get("content-range", "")  # type: ignore[attr-defined]
    if "/" in content_range:
        value = content_range.rsplit("/", 1)[-1]
        if value.isdigit():
            return int(value)
    content_length = headers.get("content-length", "")  # type: ignore[attr-defined]
    return completed + int(content_length) if str(content_length).isdigit() else 0


def _stream_requests_download(
    url: str,
    partial_path: Path,
    label: str,
    headers: dict,
) -> None:
    """Write one requests-based attempt, resuming a partial file when possible."""
    completed = partial_path.stat().st_size if partial_path.exists() else 0
    request_headers = dict(headers)
    # An open-ended range also avoids long start-up delays observed for some
    # multi-gigabyte repository objects. Servers that ignore ranges return 200
    # and are handled as ordinary fresh transfers.
    request_headers.setdefault("Range", f"bytes={completed}-")

    with requests.get(
        url,
        stream=True,
        timeout=(20, 60),
        headers=request_headers,
    ) as response:
        response.raise_for_status()
        ranged = response.status_code == 206
        append = completed > 0 and ranged
        if ranged:
            content_range = response.headers.get("content-range", "")
            if not content_range.startswith(f"bytes {completed}-"):
                raise RuntimeError(
                    "The server returned an unexpected byte range while "
                    f"resuming {partial_path.name}: {content_range or 'missing'}"
                )
        else:
            completed = 0

        total = _response_total(response.headers, completed)
        with Progress(
            TextColumn(f"[bold cyan]{label}"),
            BarColumn(),
            DownloadColumn(),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
            console=console,
        ) as progress:
            task = progress.add_task(
                "Downloading",
                total=total if total else None,
                completed=completed,
            )
            with partial_path.open("ab" if append else "wb") as handle:
                for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                    if chunk:
                        handle.write(chunk)
                        progress.advance(task, len(chunk))
        if total and partial_path.stat().st_size < total:
            raise IOError(
                f"Incomplete transfer for {partial_path.name}: "
                f"{partial_path.stat().st_size} of {total} bytes"
            )


def _stream_system_trust_download(
    url: str,
    partial_path: Path,
    label: str,
    headers: dict,
) -> None:
    """Download through urllib, which uses the operating-system trust store."""
    completed = partial_path.stat().st_size if partial_path.exists() else 0
    request_headers = dict(headers)
    request_headers.setdefault("Range", f"bytes={completed}-")
    request = urllib.request.Request(url, headers=request_headers)

    with urllib.request.urlopen(request, timeout=60) as response:
        status = getattr(response, "status", response.getcode())
        ranged = status == 206
        append = completed > 0 and ranged
        if ranged:
            content_range = response.headers.get("content-range", "")
            if not content_range.startswith(f"bytes {completed}-"):
                raise RuntimeError(
                    "The server returned an unexpected byte range while "
                    f"resuming {partial_path.name}: {content_range or 'missing'}"
                )
        else:
            completed = 0

        total = _response_total(response.headers, completed)
        with Progress(
            TextColumn(f"[bold cyan]{label}"),
            BarColumn(),
            DownloadColumn(),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
            console=console,
        ) as progress:
            task = progress.add_task(
                "Downloading",
                total=total if total else None,
                completed=completed,
            )
            with partial_path.open("ab" if append else "wb") as handle:
                while True:
                    chunk = response.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    handle.write(chunk)
                    progress.advance(task, len(chunk))
        if total and partial_path.stat().st_size < total:
            raise IOError(
                f"Incomplete transfer for {partial_path.name}: "
                f"{partial_path.stat().st_size} of {total} bytes"
            )


def download_file(
    url: str,
    dest_path: str | Path,
    desc: Optional[str] = None,
    expected_md5: Optional[str] = None,
    headers: Optional[dict] = None,
) -> Path:
    """
    Download a file from a URL with a rich progress bar.

    Args:
        url: Source URL
        dest_path: Destination file path
        desc: Description shown in progress bar
        expected_md5: If provided, verify checksum after download

    Returns:
        Path to the downloaded file
    """
    dest_path = Path(dest_path)
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    label = desc or dest_path.name
    partial_path = dest_path.with_name(f"{dest_path.name}.part")
    last_error: Optional[Exception] = None

    for attempt in range(1, DOWNLOAD_ATTEMPTS + 1):
        try:
            try:
                _stream_requests_download(
                    url,
                    partial_path,
                    label,
                    headers or {},
                )
            except requests.exceptions.SSLError:
                console.print(
                    "[yellow]Certificate validation through requests failed; "
                    "retrying with the operating-system trust store.[/]"
                )
                _stream_system_trust_download(
                    url,
                    partial_path,
                    label,
                    headers or {},
                )
            last_error = None
            break
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception as exc:
            last_error = exc
            status_code = None
            if isinstance(exc, requests.exceptions.HTTPError):
                status_code = (
                    exc.response.status_code
                    if exc.response is not None
                    else None
                )
            elif isinstance(exc, urllib.error.HTTPError):
                status_code = exc.code
            if (
                status_code is not None
                and 400 <= status_code < 500
                and status_code not in {408, 425, 429}
            ):
                raise
            if attempt == DOWNLOAD_ATTEMPTS:
                raise
            console.print(
                f"[yellow]Download attempt {attempt}/{DOWNLOAD_ATTEMPTS} "
                f"failed for {label}: {exc}. Retrying from the partial file.[/]"
            )

    if last_error is not None:
        raise last_error
    partial_path.replace(dest_path)

    if expected_md5:
        md5 = hashlib.md5()
        with dest_path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(CHUNK_SIZE), b""):
                md5.update(chunk)
        actual = md5.hexdigest()
        if actual != expected_md5:
            dest_path.unlink(missing_ok=True)
            raise ValueError(
                f"Checksum mismatch for {dest_path.name}.\n"
                f"Expected: {expected_md5}\n"
                f"Got:      {actual}"
            )
        console.print(f"[green]Checksum verified: {actual}[/]")

    return dest_path


def _is_supported_archive(path: str | Path) -> bool:
    name = Path(path).name.lower()
    return any(
        name.endswith(extension)
        for extension in (
            ".zip",
            ".tar.gz",
            ".tgz",
            ".tar.bz2",
            ".tar.xz",
            ".tar",
            ".rar",
            ".7z",
        )
    )


def extract_archive(archive_path: str | Path, extract_to: str | Path) -> None:
    """
    Safely extract a ZIP, TAR, RAR, or 7z archive.

    Args:
        archive_path: Path to the archive file
        extract_to: Directory to extract into
    """
    archive_path = Path(archive_path)
    extract_to = Path(extract_to)
    extract_to.mkdir(parents=True, exist_ok=True)

    name = archive_path.name.lower()
    console.print(f"[dim]Extracting {archive_path.name}...[/]")

    def _safe_destination(member_name: str) -> Path:
        candidate = (extract_to / member_name).resolve()
        root = extract_to.resolve()
        if candidate != root and root not in candidate.parents:
            raise ValueError(f"Archive member escapes destination: {member_name}")
        return candidate

    def _validate_tar_members(members: List[tarfile.TarInfo]) -> None:
        for member in members:
            _safe_destination(member.name)
            # Link targets can escape after extraction even when the member
            # name itself is safe. Dataset archives do not need links or
            # device nodes, so reject them rather than resolving ambiguously.
            if member.issym() or member.islnk() or member.isdev():
                raise ValueError(
                    f"Archive member type is not permitted: {member.name}"
                )

    def _extract_with_system_tar() -> None:
        executable = shutil.which("tar")
        if not executable:
            raise ValueError(
                f"Unsupported archive format: {archive_path.suffix}. "
                "Install bsdtar/libarchive or 7-Zip to extract this archive."
            )

        listing = subprocess.run(
            [executable, "-tf", str(archive_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        if listing.returncode != 0:
            raise ValueError(
                f"Could not list {archive_path.name} with {Path(executable).name}: "
                f"{(listing.stderr or listing.stdout).strip()}"
            )
        members = [line for line in listing.stdout.splitlines() if line]
        if not members:
            raise ValueError(f"Archive contains no members: {archive_path.name}")
        for member_name in members:
            _safe_destination(member_name)

        verbose = subprocess.run(
            [executable, "-tvf", str(archive_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        if verbose.returncode != 0:
            raise ValueError(
                f"Could not inspect {archive_path.name} with "
                f"{Path(executable).name}: "
                f"{(verbose.stderr or verbose.stdout).strip()}"
            )
        for line in verbose.stdout.splitlines():
            if line and line[0].lower() in {"l", "h", "b", "c", "p", "s"}:
                raise ValueError(
                    "Archive links and special files are not permitted: "
                    f"{line}"
                )

        extraction = subprocess.run(
            [executable, "-xf", str(archive_path), "-C", str(extract_to)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        if extraction.returncode != 0:
            raise ValueError(
                f"Could not extract {archive_path.name} with "
                f"{Path(executable).name}: "
                f"{(extraction.stderr or extraction.stdout).strip()}"
            )

    if name.endswith(".zip"):
        try:
            with zipfile.ZipFile(archive_path, "r") as zf:
                for member in zf.infolist():
                    _safe_destination(member.filename)
                zf.extractall(extract_to)
        except zipfile.BadZipFile:
            # Some sources publish an ordinary ZIP split into numbered byte
            # ranges. After reassembly, libarchive is more tolerant of the
            # original multi-volume metadata than Python's zipfile module.
            _extract_with_system_tar()

    elif name.endswith(".tar.gz") or name.endswith(".tgz"):
        with tarfile.open(archive_path, "r:gz") as tf:
            _validate_tar_members(tf.getmembers())
            tf.extractall(extract_to)

    elif name.endswith(".tar.bz2"):
        with tarfile.open(archive_path, "r:bz2") as tf:
            _validate_tar_members(tf.getmembers())
            tf.extractall(extract_to)

    elif name.endswith(".tar.xz"):
        with tarfile.open(archive_path, "r:xz") as tf:
            _validate_tar_members(tf.getmembers())
            tf.extractall(extract_to)

    elif name.endswith(".tar"):
        with tarfile.open(archive_path, "r:") as tf:
            _validate_tar_members(tf.getmembers())
            tf.extractall(extract_to)

    elif name.endswith(".rar") or name.endswith(".7z"):
        _extract_with_system_tar()

    else:
        raise ValueError(f"Unsupported archive format: {archive_path.suffix}")

    console.print(f"[green]Extracted to {extract_to}[/]")


def download_kaggle(
    competition_or_dataset: str,
    dest_dir: str | Path,
    is_competition: bool = False,
) -> None:
    """
    Download a Kaggle competition or dataset using the Kaggle API.

    Requires KAGGLE_USERNAME and KAGGLE_KEY environment variables, or a
    kaggle.json file at ~/.kaggle/kaggle.json.

    Args:
        competition_or_dataset: Competition slug or "owner/dataset-slug"
        dest_dir: Directory to save the downloaded files
        is_competition: True for competition data, False for dataset
    """
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Load .env file if present (sets KAGGLE_USERNAME / KAGGLE_KEY without
    # overriding values already present in the environment)
    _load_dotenv()

    # Check for credentials
    has_env = os.environ.get("KAGGLE_USERNAME") and os.environ.get("KAGGLE_KEY")
    kaggle_json = Path.home() / ".kaggle" / "kaggle.json"
    has_json = kaggle_json.exists()

    if not has_env and not has_json:
        console.print(
            Panel(
                "[bold red]Kaggle credentials not found.[/]\n\n"
                "Easiest setup — create a [bold].env[/] file in your project root:\n\n"
                "  [bold]cp .env.example .env[/]\n\n"
                "Then edit [bold].env[/] and fill in:\n"
                "  [bold]KAGGLE_USERNAME=your_username[/]\n"
                "  [bold]KAGGLE_KEY=your_api_key[/]\n\n"
                "Get your API key at [bold]https://www.kaggle.com[/] → Account → API → Create New Token\n\n"
                "Alternative options:\n"
                "  • Save kaggle.json to [bold]~/.kaggle/kaggle.json[/]\n"
                "  • Export env vars: [bold]export KAGGLE_USERNAME=... KAGGLE_KEY=...[/]\n\n"
                f"Then re-run: [bold]eyehub download --datasets {competition_or_dataset}[/]",
                title="Kaggle Authentication Required",
                border_style="red",
            )
        )
        raise RuntimeError(
            "Kaggle credentials not found. See instructions above."
        )

    try:
        import kaggle  # noqa: F401
    except ImportError:
        raise ImportError(
            "kaggle package not installed. Run: pip install eyedatahub[kaggle]"
        )

    # kaggle ≥2.0 exposes a pre-built `api` singleton and renamed the class
    # to KaggleApi; older versions used KaggleApiExtended.
    try:
        from kaggle import api
        api.authenticate()
    except ImportError:
        try:
            from kaggle.api.kaggle_api_extended import KaggleApiExtended
            api = KaggleApiExtended()
            api.authenticate()
        except ImportError:
            from kaggle import KaggleApi
            api = KaggleApi()
            api.authenticate()

    if is_competition:
        console.print(f"[cyan]Downloading competition: {competition_or_dataset}[/]")
        api.competition_download_files(
            competition_or_dataset, path=str(dest_dir), quiet=False
        )
    else:
        console.print(f"[cyan]Downloading dataset: {competition_or_dataset}[/]")
        api.dataset_download_files(
            competition_or_dataset, path=str(dest_dir), unzip=True, quiet=False
        )

    console.print(f"[green]Kaggle download complete: {dest_dir}[/]")


def download_gdrive(file_id: str, dest_path: str | Path) -> None:
    """
    Download a file from Google Drive using gdown.

    Args:
        file_id: Google Drive file ID (from sharing URL)
        dest_path: Destination file path
    """
    try:
        import gdown
    except ImportError:
        raise ImportError("gdown not installed. Run: pip install gdown")

    dest_path = Path(dest_path)
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    url = f"https://drive.google.com/uc?id={file_id}"
    console.print(f"[cyan]Downloading from Google Drive: {file_id}[/]")
    gdown.download(url, str(dest_path), quiet=False)
    console.print(f"[green]Downloaded to {dest_path}[/]")


def download_gdrive_folder(folder_id: str, dest_dir: str | Path) -> None:
    """
    Download an entire Google Drive folder using gdown.

    Args:
        folder_id: Google Drive folder ID (last segment of the sharing URL)
        dest_dir:  Directory to download files into
    """
    try:
        import gdown
    except ImportError:
        raise ImportError("gdown not installed. Run: pip install gdown")

    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    console.print(f"[cyan]Downloading GDrive folder: {folder_id}[/]")
    gdown.download_folder(
        id=folder_id,
        output=str(dest_dir),
        quiet=False,
        use_cookies=False,
    )
    console.print(f"[green]GDrive folder downloaded to {dest_dir}[/]")


def download_github_repo(
    repo: str,
    dest_dir: str | Path,
    branch: str = "main",
) -> None:
    """
    Download a GitHub repository as a ZIP archive and extract it.

    Args:
        repo:     GitHub repo in "owner/name" format
        dest_dir: Directory to extract the repository into
        branch:   Branch/tag to download (default: "main")
    """
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    zip_url = f"https://github.com/{repo}/archive/refs/heads/{branch}.zip"
    zip_path = dest_dir / f"{repo.replace('/', '_')}_{branch}.zip"

    console.print(f"[cyan]Downloading GitHub repo {repo} ({branch})...[/]")
    download_file(zip_url, zip_path, desc=f"{repo} ({branch})")
    extract_archive(zip_path, dest_dir)
    zip_path.unlink(missing_ok=True)
    console.print(f"[green]Repo extracted to {dest_dir}[/]")


def download_figshare_private(
    share_token: str,
    dest_dir: str | Path,
    extract: bool = True,
) -> List[Path]:
    """
    Download files from a private/shared Figshare article link.

    The ``share_token`` is the opaque token at the end of a Figshare private
    share URL, e.g. ``https://figshare.com/s/<share_token>``.

    Args:
        share_token: Token from the Figshare private share URL
        dest_dir:    Directory to save downloaded files.
        extract:     Automatically extract .zip/.tar.gz archives (default True).

    Returns:
        List of paths to downloaded (and optionally extracted) files.
    """
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Resolve private share → article metadata
    meta_url = f"https://api.figshare.com/v2/articles?token={share_token}"
    resp = requests.get(meta_url, timeout=30)
    articles: list = []
    if resp.ok:
        articles = resp.json() if isinstance(resp.json(), list) else []

    if not articles:
        # Alternative: fetch the private share HTML page and extract article ID
        page_resp = requests.get(
            f"https://figshare.com/s/{share_token}", timeout=30
        )
        # Look for the article ID in the redirect URL or canonical link
        import re
        match = re.search(r"/articles/[^/]+/(\d+)", page_resp.url + page_resp.text)
        if not match:
            raise RuntimeError(
                f"Could not resolve Figshare private share token '{share_token}'.\n"
                "Visit the URL manually and download the files:\n"
                f"  https://figshare.com/s/{share_token}"
            )
        article_id = match.group(1)
        articles = [{"id": int(article_id)}]

    downloaded: List[Path] = []
    for article in articles:
        article_id = article.get("id")
        files_url = f"https://api.figshare.com/v2/articles/{article_id}/files?token={share_token}"
        files_resp = requests.get(files_url, timeout=30)
        if not files_resp.ok:
            # Try without token
            files_resp = requests.get(
                f"https://api.figshare.com/v2/articles/{article_id}/files",
                timeout=30,
            )
        files_resp.raise_for_status()
        for file_info in files_resp.json():
            fname = file_info.get("name", f"file_{file_info.get('id', '0')}")
            file_url = file_info.get("download_url") or file_info.get("url", "")
            dest_path = dest_dir / fname
            if dest_path.exists():
                console.print(f"[dim]  {fname} already present, skipping.[/]")
                downloaded.append(dest_path)
                continue
            console.print(f"[cyan]  Downloading {fname} (Figshare private share)...[/]")
            download_file(file_url, dest_path, desc=fname)
            downloaded.append(dest_path)
            if extract and _is_supported_archive(fname):
                try:
                    extract_archive(dest_path, dest_dir)
                except Exception as e:
                    console.print(f"[yellow]  Could not auto-extract {fname}: {e}[/]")

    return downloaded


def download_zenodo(
    record_id: str | int,
    dest_dir: str | Path,
    filename: Optional[str] = None,
    token: Optional[str] = None,
    extract: bool = True,
) -> List[Path]:
    """
    Download files from a Zenodo record, with optional token authentication
    for restricted / embargoed records.

    Args:
        record_id:  Zenodo record ID — the number at the end of
                    https://zenodo.org/records/XXXXXX
        dest_dir:   Directory to save downloaded files.
        filename:   If given, download only this specific file; otherwise
                    download all files in the record.
        token:      Zenodo personal access token.  If None, falls back to
                    the ZENODO_TOKEN environment variable.
                    Create one at https://zenodo.org/account/settings/applications/
        extract:    Automatically extract .zip/.tar.gz archives (default True).

    Returns:
        List of paths to downloaded (and optionally extracted) files.

    Example::

        from eyedatahub.datasets.download_utils import download_zenodo
        download_zenodo("5880419", "/data/corn1500")
        download_zenodo("14263883", "/data/corn2", token="my_token")
    """
    _load_dotenv()
    token = token or os.environ.get("ZENODO_TOKEN")

    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    headers: dict = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    # Fetch record metadata
    api_url = f"https://zenodo.org/api/records/{record_id}"
    console.print(f"[cyan]Fetching Zenodo record {record_id}...[/]")
    resp = requests.get(api_url, headers=headers, timeout=30)
    if resp.status_code == 401:
        raise PermissionError(
            f"Zenodo record {record_id} requires authentication.\n"
            "Add ZENODO_TOKEN to your .env file:\n"
            "  ZENODO_TOKEN=your_token\n"
            "Create a token at: https://zenodo.org/account/settings/applications/"
        )
    if resp.status_code == 403:
        raise PermissionError(
            f"Zenodo record {record_id} is restricted. "
            "Your token may not have access, or the record requires a request."
        )
    resp.raise_for_status()

    record = resp.json()
    files = record.get("files", [])
    if not files:
        # Try the newer /api/records/{id}/files endpoint
        files_resp = requests.get(
            f"https://zenodo.org/api/records/{record_id}/files",
            headers=headers, timeout=30
        )
        files_resp.raise_for_status()
        files = files_resp.json().get("entries", files_resp.json())

    if filename:
        files = [f for f in files if f.get("key", f.get("filename", "")) == filename]
        if not files:
            available = [f.get("key", f.get("filename", "?")) for f in record.get("files", [])]
            raise FileNotFoundError(
                f"File '{filename}' not found in Zenodo record {record_id}.\n"
                f"Available files: {available}"
            )

    downloaded: List[Path] = []
    for file_info in files:
        fname = file_info.get("key") or file_info.get("filename") or file_info.get("name", "file")
        # Support both old and new Zenodo API response shapes
        file_url = (
            file_info.get("links", {}).get("self")
            or file_info.get("links", {}).get("download")
            or f"https://zenodo.org/records/{record_id}/files/{fname}"
        )

        dest_path = dest_dir / fname
        if dest_path.exists():
            console.print(f"[dim]  {fname} already present, skipping.[/]")
            downloaded.append(dest_path)
            continue

        console.print(f"[cyan]  Downloading {fname} from Zenodo {record_id}...[/]")
        # Stream download with auth header
        dl_headers = {"Authorization": f"Bearer {token}"} if token else {}
        download_file(file_url, dest_path, desc=fname, headers=dl_headers)
        downloaded.append(dest_path)

        if extract and _is_supported_archive(dest_path):
            try:
                extract_archive(dest_path, dest_dir)
            except Exception as e:
                console.print(f"[yellow]  Could not auto-extract {fname}: {e}[/]")

    return downloaded


def download_figshare(
    article_id: str | int,
    dest_dir: str | Path,
    filename: Optional[str] = None,
    token: Optional[str] = None,
    extract: bool = True,
) -> List[Path]:
    """
    Download files from a Figshare article, with optional token authentication
    for private/restricted articles.

    Args:
        article_id: Figshare article ID — the number at the end of
                    https://figshare.com/articles/XXXXXX
        dest_dir:   Directory to save downloaded files.
        filename:   If given, download only this specific file; otherwise
                    download all files in the article.
        token:      Figshare personal token.  If None, falls back to the
                    FIGSHARE_TOKEN environment variable.
                    Create one at https://figshare.com/account/applications
        extract:    Automatically extract .zip/.tar.gz archives (default True).

    Returns:
        List of paths to downloaded (and optionally extracted) files.

    Example::

        from eyedatahub.datasets.download_utils import download_figshare
        download_figshare("12345678", "/data/my_dataset")
    """
    _load_dotenv()
    token = token or os.environ.get("FIGSHARE_TOKEN")

    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    headers: dict = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"token {token}"

    api_url = f"https://api.figshare.com/v2/articles/{article_id}/files"
    console.print(f"[cyan]Fetching Figshare article {article_id}...[/]")
    resp = requests.get(api_url, headers=headers, timeout=30)
    if resp.status_code == 403:
        raise PermissionError(
            f"Figshare article {article_id} is restricted.\n"
            "Add FIGSHARE_TOKEN to your .env file:\n"
            "  FIGSHARE_TOKEN=your_token\n"
            "Create a token at: https://figshare.com/account/applications"
        )
    resp.raise_for_status()

    files = resp.json()
    if filename:
        files = [f for f in files if f.get("name", "") == filename]
        if not files:
            raise FileNotFoundError(
                f"File '{filename}' not found in Figshare article {article_id}."
            )

    downloaded: List[Path] = []
    for file_info in files:
        fname = file_info.get("name", f"file_{file_info.get('id', '0')}")
        file_url = file_info.get("download_url") or file_info.get("url", "")

        dest_path = dest_dir / fname
        if dest_path.exists():
            console.print(f"[dim]  {fname} already present, skipping.[/]")
            downloaded.append(dest_path)
            continue

        console.print(f"[cyan]  Downloading {fname} from Figshare {article_id}...[/]")
        download_file(file_url, dest_path, desc=fname)
        downloaded.append(dest_path)

        if extract and _is_supported_archive(fname):
            try:
                extract_archive(dest_path, dest_dir)
            except Exception as e:
                console.print(f"[yellow]  Could not auto-extract {fname}: {e}[/]")

    return downloaded


def download_figshare_collection(
    collection_id: str | int,
    dest_dir: str | Path,
    *,
    token: Optional[str] = None,
    extract: bool = True,
) -> List[Path]:
    """Download every public article in a Figshare collection.

    Figshare collection DOIs (``m9.figshare.c.<id>``) are not article IDs.
    This helper resolves collection membership through the public API and then
    delegates each transfer to :func:`download_figshare`.
    """
    _load_dotenv()
    token = token or os.environ.get("FIGSHARE_TOKEN")
    headers: dict = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"token {token}"
    response = requests.get(
        f"https://api.figshare.com/v2/collections/{collection_id}/articles",
        headers=headers,
        params={"page_size": 1000},
        timeout=30,
    )
    response.raise_for_status()
    articles = response.json()
    if not articles:
        raise FileNotFoundError(
            f"Figshare collection {collection_id} contains no public articles."
        )
    root = Path(dest_dir)
    downloaded: List[Path] = []
    for article in sorted(articles, key=lambda item: int(item["id"])):
        downloaded.extend(
            download_figshare(
                article["id"],
                root / f"article_{article['id']}",
                token=token,
                extract=extract,
            )
        )
    return downloaded


def download_dryad(
    doi: str,
    dest_dir: str | Path,
    extract: bool = True,
    token: Optional[str] = None,
) -> List[Path]:
    """Download all files from the latest public version of a Dryad dataset.

    Args:
        doi: Dryad DOI, with or without the ``doi:`` prefix.
        dest_dir: Directory in which to preserve the Dryad file paths.
        extract: Automatically extract supported archives (default True).
        token: Optional Dryad bearer token. Large records that exceed Dryad's
            public ZIP limit require authenticated per-file API downloads.

    Returns:
        Paths to the downloaded files.
    """
    _load_dotenv()
    token = token or os.environ.get("DRYAD_TOKEN")
    headers = {"Authorization": f"Bearer {token}"} if token else {}

    def refresh_token() -> None:
        """Refresh an expired bearer token without persisting or printing it."""
        nonlocal token, headers
        client_id = os.environ.get("DRYAD_CLIENT_ID")
        client_secret = os.environ.get("DRYAD_SECRET")
        if not client_id or not client_secret:
            raise RuntimeError(
                "The Dryad token was rejected. Set a current DRYAD_TOKEN or "
                "configure DRYAD_CLIENT_ID and DRYAD_SECRET for automatic renewal."
            )
        token_response = requests.post(
            "https://datadryad.org/oauth/token",
            data={
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": "client_credentials",
            },
            headers={"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"},
            timeout=30,
        )
        token_response.raise_for_status()
        token = str(token_response.json().get("access_token") or "").strip()
        if not token:
            raise RuntimeError("Dryad returned no access token.")
        headers = {"Authorization": f"Bearer {token}"}

    if not token and os.environ.get("DRYAD_CLIENT_ID") and os.environ.get("DRYAD_SECRET"):
        refresh_token()

    def dryad_get(url: str) -> requests.Response:
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 401:
            refresh_token()
            response = requests.get(url, headers=headers, timeout=30)
        return response

    def dryad_download(url: str, destination: Path, description: str) -> Path:
        try:
            return download_file(
                url,
                destination,
                desc=description,
                headers=headers,
            )
        except requests.exceptions.HTTPError as exc:
            if exc.response is None or exc.response.status_code != 401:
                raise
            refresh_token()
            return download_file(
                url,
                destination,
                desc=description,
                headers=headers,
            )

    identifier = doi if doi.startswith("doi:") else f"doi:{doi}"
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    encoded_identifier = quote(identifier, safe="")
    dataset_url = (
        "https://datadryad.org/api/v2/datasets/" f"{encoded_identifier}"
    )
    console.print(f"[cyan]Fetching Dryad dataset {identifier[4:]}...[/]")
    response = dryad_get(dataset_url)
    if response.status_code == 404:
        raise FileNotFoundError(
            f"Dryad dataset '{identifier[4:]}' was not found.\n"
            f"Check https://datadryad.org/dataset/{encoded_identifier}"
        )
    response.raise_for_status()

    version_href = (
        response.json().get("_links", {}).get("stash:version", {}).get("href")
    )
    if not version_href:
        raise RuntimeError(
            f"Dryad did not expose a latest-version link for {identifier[4:]}"
        )

    version_url = f"https://datadryad.org{version_href}"
    version_response = dryad_get(version_url)
    version_response.raise_for_status()
    version_payload = version_response.json()
    version_download_href = (
        version_payload.get("_links", {})
        .get("stash:download", {})
        .get("href")
    )
    if version_download_href:
        version_download_url = (
            version_download_href
            if version_download_href.startswith("http")
            else f"https://datadryad.org{version_download_href}"
        )
        archive = dest_dir / "dryad-version.zip"
        console.print(
            f"[cyan]  Downloading the public Dryad version archive for "
            f"{identifier[4:]}...[/]"
        )
        try:
            dryad_download(
                version_download_url,
                archive,
                f"Dryad {identifier[4:]}",
            )
        except requests.exceptions.HTTPError as exc:
            if exc.response is None or exc.response.status_code != 405:
                raise
            archive.unlink(missing_ok=True)
            console.print(
                "[yellow]  Dryad does not assemble a whole-version ZIP for "
                "this record; falling back to its per-file API.[/]"
            )
        else:
            if not extract:
                return [archive]
            extract_archive(archive, dest_dir)
            archive.unlink(missing_ok=True)
            extracted = sorted(
                path for path in dest_dir.rglob("*") if path.is_file()
            )
            if not extracted:
                raise RuntimeError(
                    f"Dryad version archive for {identifier[4:]} was empty."
                )
            return extracted

    files_href = (
        version_payload
        .get("_links", {})
        .get("stash:files", {})
        .get("href")
    )
    if not files_href:
        raise RuntimeError(
            f"Dryad did not expose a file listing for {identifier[4:]}"
        )

    files: list[dict] = []
    next_href: Optional[str] = files_href
    while next_href:
        files_url = (
            next_href
            if next_href.startswith("http")
            else f"https://datadryad.org{next_href}"
        )
        files_response = dryad_get(files_url)
        files_response.raise_for_status()
        payload = files_response.json()
        files.extend(payload.get("_embedded", {}).get("stash:files", []))
        next_href = payload.get("_links", {}).get("next", {}).get("href")

    downloaded: List[Path] = []
    if files and not token:
        raise RuntimeError(
            "Dryad does not provide a whole-version archive for "
            f"{identifier[4:]}. Its per-file API requires a bearer token. "
            "Set DRYAD_TOKEN or download the files from the official Dryad "
            "landing page."
        )

    for file_info in files:
        relative_path = Path(file_info.get("path") or "file")
        if relative_path.is_absolute() or ".." in relative_path.parts:
            raise ValueError(
                f"Unsafe path in Dryad record {identifier[4:]}: {relative_path}"
            )

        download_href = (
            file_info.get("_links", {})
            .get("stash:download", {})
            .get("href")
        )
        if not download_href:
            continue
        file_url = (
            download_href
            if download_href.startswith("http")
            else f"https://datadryad.org{download_href}"
        )
        dest_path = dest_dir / relative_path
        if dest_path.exists():
            console.print(
                f"[dim]  {relative_path.as_posix()} already present, skipping.[/]"
            )
            downloaded.append(dest_path)
            continue

        console.print(
            f"[cyan]  Downloading {relative_path.as_posix()} from Dryad...[/]"
        )
        dryad_download(
            file_url,
            dest_path,
            relative_path.name,
        )
        downloaded.append(dest_path)

        name = dest_path.name.lower()
        if extract and _is_supported_archive(name):
            try:
                extract_archive(dest_path, dest_path.parent)
            except Exception as exc:
                console.print(
                    f"[yellow]  Could not auto-extract {dest_path.name}: {exc}[/]"
                )

    return downloaded


def download_mendeley(
    dataset_id: str,
    version: int,
    dest_dir: str | Path,
    token: Optional[str] = None,
    extract: bool = True,
) -> List[Path]:
    """
    Download files from a Mendeley Data dataset.

    Args:
        dataset_id: Mendeley dataset ID (e.g. "sncdhf53xc")
        version:    Dataset version number (e.g. 1)
        dest_dir:   Directory to save downloaded files.
        token:      Mendeley API token (optional; falls back to MENDELEY_TOKEN env var).
                    Not required for publicly accessible datasets.
        extract:    Automatically extract .zip/.tar.gz archives (default True).

    Returns:
        List of paths to downloaded (and optionally extracted) files.

    Example::

        from eyedatahub.datasets.download_utils import download_mendeley
        download_mendeley("sncdhf53xc", 4, "/data/octdl")
    """
    _load_dotenv()
    token = token or os.environ.get("MENDELEY_TOKEN")

    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    encoded_id = quote(dataset_id, safe="")
    api_url = f"https://api.data.mendeley.com/datasets/publics/{encoded_id}/files"
    console.print(f"[cyan]Fetching Mendeley dataset {dataset_id} v{version}...[/]")

    headers: dict = {
        "Accept": "application/vnd.mendeley-public-dataset.1+json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    files: list[dict] = []
    start = 0
    limit = 100
    while True:
        resp = requests.get(
            api_url,
            headers=headers,
            params={"version": version, "$start": start, "$limit": limit},
            timeout=30,
        )
        if resp.status_code in (401, 403):
            raise PermissionError(
                f"Mendeley Data API access for '{dataset_id}' v{version} requires "
                "platform credentials, a compatible client, or access setup.\n"
                "This response does not establish that the dataset is unavailable.\n"
                f"Use the source page: https://data.mendeley.com/datasets/{dataset_id}/{version}"
            )
        if resp.status_code == 404:
            raise FileNotFoundError(
                f"Mendeley dataset '{dataset_id}' version {version} not found.\n"
                f"Check https://data.mendeley.com/datasets/{dataset_id}/{version}"
            )
        resp.raise_for_status()

        payload = resp.json()
        if isinstance(payload, list):
            batch = payload
        elif isinstance(payload, dict):
            batch = payload.get("results", payload.get("files", payload.get("data", [])))
            if isinstance(batch, dict):
                batch = batch.get("results", batch.get("files", []))
        else:
            batch = []
        if not isinstance(batch, list):
            raise RuntimeError(
                f"Unexpected Mendeley API response for '{dataset_id}' v{version}."
            )
        files.extend(item for item in batch if isinstance(item, dict))
        if len(batch) < limit:
            break
        start += len(batch)

    if not files:
        raise RuntimeError(
            f"Mendeley returned no files for '{dataset_id}' v{version}.\n"
            f"Verify the release at https://data.mendeley.com/datasets/{dataset_id}/{version}"
        )

    downloaded: List[Path] = []
    for file_info in files:
        raw_name = file_info.get("filename") or file_info.get("name") or file_info.get("id") or "file"
        fname = Path(str(raw_name)).name
        # Public file records normally expose a short-lived direct URL.
        file_url = (
            file_info.get("download_url")
            or file_info.get("content_details", {}).get("download_url")
            or (
                f"https://api.data.mendeley.com/datasets/{encoded_id}/files/"
                f"{quote(str(file_info.get('id', '')), safe='')}/file_downloaded"
                f"?version={version}"
            )
        )

        dest_path = dest_dir / fname
        if dest_path.exists():
            console.print(f"[dim]  {fname} already present, skipping.[/]")
            downloaded.append(dest_path)
            continue

        console.print(f"[cyan]  Downloading {fname} from Mendeley...[/]")
        download_file(file_url, dest_path, desc=fname)
        downloaded.append(dest_path)

        if extract and _is_supported_archive(fname):
            try:
                extract_archive(dest_path, dest_dir)
            except Exception as e:
                console.print(f"[yellow]  Could not auto-extract {fname}: {e}[/]")

    return downloaded


def download_dataverse(
    persistent_id: str,
    dest_dir: str | Path,
    server: str = "https://dataverse.harvard.edu",
    token: Optional[str] = None,
    extract: bool = True,
) -> List[Path]:
    """
    Download a dataset from a Dataverse repository (Harvard Dataverse or compatible).

    Args:
        persistent_id: Dataverse persistent ID, e.g. "doi:10.7910/DVN/1YRRAC"
        dest_dir:      Directory to save downloaded files.
        server:        Dataverse server URL (default: Harvard Dataverse).
        token:         API token. Falls back to DATAVERSE_TOKEN env var.
                       Required for restricted datasets.
        extract:       Automatically extract .zip/.tar.gz archives (default True).

    Returns:
        List of paths to downloaded (and optionally extracted) files.

    Example::

        from eyedatahub.datasets.download_utils import download_dataverse
        download_dataverse("doi:10.7910/DVN/1YRRAC", "/data/harvard_glaucoma")
    """
    _load_dotenv()
    token = token or os.environ.get("DATAVERSE_TOKEN")

    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    headers: dict = {"Accept": "application/json"}
    if token:
        headers["X-Dataverse-key"] = token

    # Fetch file listing for latest version
    api_url = (
        f"{server}/api/datasets/:persistentId/versions/:latest/files"
        f"?persistentId={persistent_id}"
    )
    console.print(f"[cyan]Fetching Dataverse dataset {persistent_id}...[/]")
    resp = requests.get(api_url, headers=headers, timeout=30)
    if resp.status_code in (401, 403):
        raise PermissionError(
            f"Dataverse dataset {persistent_id} requires authentication.\n"
            "Add DATAVERSE_TOKEN to your .env file:\n"
            "  DATAVERSE_TOKEN=your_token\n"
            f"Get a token at: {server}/dataverseuser.xhtml"
        )
    resp.raise_for_status()

    data = resp.json().get("data", [])
    downloaded: List[Path] = []

    for file_info in data:
        df = file_info.get("dataFile", {})
        file_id = df.get("id")
        fname = df.get("filename") or df.get("label", f"file_{file_id}")
        if not file_id:
            continue

        dest_path = dest_dir / fname
        if dest_path.exists():
            console.print(f"[dim]  {fname} already present, skipping.[/]")
            downloaded.append(dest_path)
            continue

        file_url = f"{server}/api/access/datafile/{file_id}"
        console.print(f"[cyan]  Downloading {fname} from Dataverse...[/]")
        dl_headers = {"X-Dataverse-key": token} if token else {}
        download_file(file_url, dest_path, desc=fname, headers=dl_headers)
        downloaded.append(dest_path)

        if extract and _is_supported_archive(fname):
            try:
                extract_archive(dest_path, dest_dir)
            except Exception as e:
                console.print(f"[yellow]  Could not auto-extract {fname}: {e}[/]")

    return downloaded


def download_huggingface(
    dataset_id: str,
    dest_dir: str | Path,
    repo_type: str = "dataset",
    token: Optional[str] = None,
) -> None:
    """
    Download a HuggingFace dataset (or model repo) using huggingface_hub.

    Args:
        dataset_id: HuggingFace dataset ID, e.g. "gOLIVES/OLIVES_Dataset"
        dest_dir:   Local directory to download files into.
        repo_type:  "dataset" (default) or "model" or "space".
        token:      HuggingFace API token; falls back to HF_TOKEN env var.
                    Required for private/gated datasets.

    Example::

        from eyedatahub.datasets.download_utils import download_huggingface
        download_huggingface("gOLIVES/OLIVES_Dataset", "/data/olives")
    """
    try:
        from huggingface_hub import snapshot_download
    except ImportError:
        raise ImportError(
            "huggingface_hub is not installed. "
            "Run: pip install huggingface_hub"
        )

    _load_dotenv()
    token = token or os.environ.get("HF_TOKEN")

    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    console.print(f"[cyan]Downloading HuggingFace {repo_type}: {dataset_id}[/]")
    snapshot_download(
        repo_id=dataset_id,
        repo_type=repo_type,
        local_dir=str(dest_dir),
        token=token,
        ignore_patterns=["*.git*", ".gitattributes"],
    )
    console.print(f"[green]HuggingFace download complete: {dest_dir}[/]")


def download_physionet(
    slug: str,
    version: str,
    dest_dir: str | Path,
    credentialed: bool = False,
    extract: bool = True,
) -> Path:
    """
    Download a PhysioNet record as a single zip archive.

    Open-access records (e.g. HYGD) use a public URL. Credentialed records
    (BRSET, mBRSET) require HTTP Basic Auth via PHYSIONET_USERNAME +
    PHYSIONET_PASSWORD environment variables — the user must independently
    complete CITI training + sign the DUA on physionet.org before their
    credentials will grant download access.

    Args:
        slug: PhysioNet project slug (e.g. "hillel-yaffe-glaucoma-dataset").
        version: Project version (e.g. "1.1.0").
        dest_dir: Where to save the extracted dataset.
        credentialed: If True, send HTTP Basic Auth with PHYSIONET_USERNAME +
                      PHYSIONET_PASSWORD env vars.
        extract: Extract the downloaded archive (default True).

    Returns:
        Path to the downloaded (and optionally extracted) directory.
    """
    _load_dotenv()
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    zip_url = (
        f"https://physionet.org/static/published-projects/{slug}/"
        f"{slug}-{version}.zip"
    )
    zip_path = dest_dir / f"{slug}-{version}.zip"

    auth = None
    if credentialed:
        user = os.environ.get("PHYSIONET_USERNAME")
        pwd = os.environ.get("PHYSIONET_PASSWORD")
        if not (user and pwd):
            raise RuntimeError(
                f"PhysioNet credentialed dataset '{slug}' requires "
                "PHYSIONET_USERNAME and PHYSIONET_PASSWORD in your .env file.\n"
                "1. Register at https://physionet.org/\n"
                "2. Complete CITI 'Data or Specimens Only Research' training\n"
                "3. Sign the dataset's Data Use Agreement on its project page\n"
                "4. Add the credentials to .env (see .env.example)"
            )
        auth = (user, pwd)

    console.print(f"[cyan]Downloading PhysioNet record: {slug} v{version}[/]")
    with requests.get(zip_url, stream=True, timeout=60, auth=auth) as resp:
        if resp.status_code == 401:
            raise PermissionError(
                f"PhysioNet returned 401 for {slug}. Credentials missing/invalid "
                "or you have not signed the DUA on the project page."
            )
        resp.raise_for_status()
        total = int(resp.headers.get("content-length", 0))
        with Progress(
            TextColumn(f"[bold cyan]{slug}-{version}.zip"),
            BarColumn(),
            DownloadColumn(),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
            console=console,
        ) as progress:
            task = progress.add_task("Downloading", total=total if total else None)
            with open(zip_path, "wb") as f:
                for chunk in resp.iter_content(chunk_size=CHUNK_SIZE):
                    if chunk:
                        f.write(chunk)
                        progress.advance(task, len(chunk))

    if extract:
        try:
            extract_archive(zip_path, dest_dir)
            zip_path.unlink(missing_ok=True)
        except Exception as e:
            console.print(f"[yellow]Could not auto-extract {zip_path.name}: {e}[/]")
    return dest_dir


def print_manual_download_instructions(
    dataset_name: str,
    url: str,
    dest_dir: str | Path,
    extra_notes: str = "",
) -> None:
    """
    Print rich-formatted instructions for a dataset that requires manual download.

    Args:
        dataset_name: Human-readable dataset name
        url: URL where the dataset can be obtained
        dest_dir: Where the user should place the files
        extra_notes: Any additional instructions
    """
    console.print(
        Panel(
            f"[bold yellow]{dataset_name}[/] requires manual download.\n\n"
            f"1. Visit: [bold blue]{url}[/]\n"
            f"2. Register / agree to the license if required\n"
            f"3. Download the dataset files\n"
            f"4. Extract and place the data in:\n"
            f"   [bold]{dest_dir}[/]\n"
            + (f"\n[dim]{extra_notes}[/]" if extra_notes else ""),
            title=f"Manual Download: {dataset_name}",
            border_style="yellow",
        )
    )
