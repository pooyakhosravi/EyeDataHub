import os

from eyedatahub.utils import credentials


def test_load_credentials_reads_explicit_env_file_without_overriding(monkeypatch, tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text(
        "\n".join(
            [
                "KAGGLE_USERNAME=from_file",
                "KAGGLE_KEY=from_file_key",
                "HF_TOKEN=hf_from_file",
            ]
        ),
        encoding="utf-8",
    )

    monkeypatch.setenv("KAGGLE_USERNAME", "from_shell")
    monkeypatch.delenv("KAGGLE_KEY", raising=False)
    monkeypatch.delenv("HF_TOKEN", raising=False)

    loaded = credentials.load_credentials(
        env_file=env_file,
        login_huggingface=False,
    )

    assert loaded == env_file
    assert os.environ["KAGGLE_USERNAME"] == "from_shell"
    assert os.environ["KAGGLE_KEY"] == "from_file_key"
    assert os.environ["HF_TOKEN"] == "hf_from_file"


def test_load_credentials_uses_eyedatahub_env_file(monkeypatch, tmp_path):
    env_file = tmp_path / "private.env"
    env_file.write_text("ZENODO_TOKEN=from_private_env\n", encoding="utf-8")

    monkeypatch.setenv("EYEDATAHUB_ENV_FILE", str(env_file))
    monkeypatch.delenv("ZENODO_TOKEN", raising=False)

    loaded = credentials.load_credentials(login_huggingface=False)

    assert loaded == env_file
    assert os.environ["ZENODO_TOKEN"] == "from_private_env"


def test_load_credentials_returns_none_for_missing_explicit_file(tmp_path):
    loaded = credentials.load_credentials(
        env_file=tmp_path / "missing.env",
        login_huggingface=False,
    )

    assert loaded is None
