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
    assert (
        _classify(403, "https://data.mendeley.com/datasets/example/2")
        == "credentials_or_client_required"
    )
    assert (
        _classify(401, "https://www.kaggle.com/api/example")
        == "credentials_or_client_required"
    )
