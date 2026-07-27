import json

from click.testing import CliRunner

from eyedatahub.agent.mcp_server import call_tool
from eyedatahub.agent.planner import build_fundus_foundation_plan
from eyedatahub.cli import main


def test_fundus_foundation_plan_is_bounded_and_side_effect_free():
    plan = build_fundus_foundation_plan(
        max_pretraining_datasets=4,
        gaps=["diabetic_retinopathy", "glaucoma", "amd"],
        max_validation_per_gap=2,
    )

    assert plan["workflow"] == "fundus_foundation_model"
    assert plan["status"] == "planning_only"
    assert plan["side_effects"] == {
        "downloads_started": False,
        "access_terms_accepted": False,
        "training_started": False,
    }
    assert len(plan["pretraining_pool"]) == 4
    assert set(plan["gap_validation"]) == {
        "diabetic_retinopathy",
        "glaucoma",
        "amd",
    }
    queued = [item["name"] for item in plan["acquisition_queue"]]
    assert len(queued) == len(set(queued))

    for candidate in plan["pretraining_pool"]:
        assert candidate["modality"] == "fundus"
        assert candidate["download_type"] != "manual"
        assert candidate["license_family"] in {
            "cc0",
            "cc-by",
            "cc-by-sa",
            "mit",
            "apache",
            "odc-by",
        }
        tags = set(candidate["tags"])
        assert "derivative" not in tags
        assert not any(tag.startswith("duplicate_of_") for tag in tags)
        assert candidate["commands"]["download_after_approval"].startswith(
            f"eyehub download {candidate['name']} --data-dir "
        )
        assert candidate["loader_status"] in {"implemented", "metadata_only"}

    assert "airogs" not in {
        item["name"] for item in plan["pretraining_pool"]
    }
    ddr = next(
        item for item in plan["pretraining_pool"] if item["name"] == "ddr"
    )
    assert ddr["loader_status"] == "implemented"
    assert ddr["commands"]["preflight"].endswith("--dry-run")
    assert "dataset.load" in ddr["commands"]["python_load_after_download"]


def test_cli_and_mcp_emit_the_same_deterministic_plan():
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "agent",
            "plan-fundus-foundation",
            "--max-pretraining-datasets",
            "3",
            "--gap",
            "glaucoma",
        ],
    )
    assert result.exit_code == 0, result.output
    cli_plan = json.loads(result.output)

    mcp_plan = call_tool(
        "eyedatahub.plan_fundus_foundation_model",
        {
            "max_pretraining_datasets": 3,
            "gaps": ["glaucoma"],
        },
    )["content"]
    assert cli_plan["plan_id"] == mcp_plan["plan_id"]
    assert cli_plan["pretraining_pool"] == mcp_plan["pretraining_pool"]
