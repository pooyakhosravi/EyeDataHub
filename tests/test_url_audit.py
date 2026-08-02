from hub.audit.verify_urls import _classify, sanitize_public_url


def test_sanitize_public_url_removes_signed_query_strings() -> None:
    signed = (
        "https://example.org/archive.zip?"
        "X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Signature=secret"
    )
    assert sanitize_public_url(signed) == "https://example.org/archive.zip"


def test_sanitize_public_url_preserves_nonsensitive_query_strings() -> None:
    public = "https://example.org/files?version=2&page_size=100"
    assert sanitize_public_url(public) == public


def test_platform_auth_response_is_an_access_requirement() -> None:
    platform_urls = (
        "https://data.mendeley.com/datasets/example/2",
        "https://www.kaggle.com/api/example",
        "https://huggingface.co/datasets/example",
        "https://zenodo.org/api/records/example",
        "https://api.figshare.com/v2/articles/example",
        "https://datadryad.org/api/v2/datasets/example",
        "https://physionet.org/content/example",
    )
    for url in platform_urls:
        assert _classify(401, url) == "credentials_or_client_required"
        assert _classify(403, url) == "credentials_or_client_required"


def test_github_and_google_drive_are_not_platform_credential_routes() -> None:
    assert _classify(401, "https://github.com/example/repository") == "auth_required"
    assert _classify(403, "https://drive.google.com/file/d/example") == "forbidden"
