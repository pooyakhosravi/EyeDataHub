from hub.audit.check_release_consistency import collect_consistency_errors


def test_public_release_artifacts_describe_one_snapshot() -> None:
    assert collect_consistency_errors() == []
