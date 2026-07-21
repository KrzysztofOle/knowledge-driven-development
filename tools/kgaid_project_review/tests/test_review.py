from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pytest

from kgaid_project_review.analysis import ReviewError, analyse_documentation
from kgaid_project_review.cli import EXIT_FINDINGS, EXIT_OK, main
from kgaid_project_review.report import json_report, markdown_report

NOW = datetime(2026, 7, 20, 12, 0, tzinfo=timezone.utc)


def write_document(root: Path, name: str, front_matter: str, body: str = "# Example\n") -> Path:
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{front_matter}---\n{body}", encoding="utf-8")
    return path


def valid_metadata(identifier: str = "REQ-001", **overrides: str) -> str:
    values = {
        "document_id": identifier,
        "title": "Example",
        "document_type": "requirement",
        "status": "proposed",
        "version": "1.0",
        "owner": "Product",
        "approval_status": "pending",
        "approved_by": "",
        "approved_at": "",
    }
    values.update(overrides)
    return "\n".join(f"{key}: {value}" for key, value in values.items()) + "\n"


def report(root: Path) -> dict[str, object]:
    return analyse_documentation(root, generated_at=NOW)


def codes(result: dict[str, object]) -> set[str]:
    return {finding["code"] for finding in result["findings"]}  # type: ignore[index]


def test_empty_directory_is_a_valid_empty_inventory(tmp_path: Path) -> None:
    result = report(tmp_path)

    assert result["inventory"]["markdown_files"] == 0  # type: ignore[index]
    assert result["summary"]["errors"] == 0  # type: ignore[index]


def test_missing_directory_is_a_clear_error(tmp_path: Path) -> None:
    with pytest.raises(ReviewError, match="does not exist"):
        analyse_documentation(tmp_path / "missing")


def test_valid_managed_document_and_exclusions_are_inventoried(tmp_path: Path) -> None:
    write_document(tmp_path, "requirements/example.md", valid_metadata())
    (tmp_path / "README.md").write_text("# Index\n", encoding="utf-8")
    (tmp_path / "templates" / "draft.md").parent.mkdir(parents=True)
    (tmp_path / "templates" / "draft.md").write_text("# Draft\n", encoding="utf-8")

    result = report(tmp_path)

    assert result["inventory"]["managed_documents"] == 1  # type: ignore[index]
    assert result["inventory"]["excluded_documents"] == {"navigation-readme": 1, "template": 1}  # type: ignore[index]
    assert codes(result) == {"TRACE003"}


def test_front_matter_errors_and_missing_fields(tmp_path: Path) -> None:
    (tmp_path / "missing.md").write_text("# Missing\n", encoding="utf-8")
    write_document(tmp_path, "invalid.md", "title: [broken\n")
    write_document(tmp_path, "incomplete.md", "document_id: REQ-003\ntitle: Example\n")

    assert {"META001", "META002", "META003"} <= codes(report(tmp_path))


def test_controlled_values_and_approval_consistency(tmp_path: Path) -> None:
    write_document(tmp_path, "draft.md", valid_metadata("REQ-005", approval_status="draft"))
    write_document(
        tmp_path,
        "draft-with-details.md",
        valid_metadata(
            "REQ-006", approval_status="draft", approved_by="Person", approved_at="2026-07-20"
        ),
    )
    write_document(
        tmp_path,
        "invalid.md",
        valid_metadata(
            document_type="unsupported",
            status="retired",
            owner="Unknown",
            approval_status="awaiting",
            version="one",
        ),
    )
    write_document(
        tmp_path,
        "pending.md",
        valid_metadata("REQ-002", approved_by="Person", approved_at="2026-07-20"),
    )
    write_document(
        tmp_path,
        "approved.md",
        valid_metadata(
            "REQ-003", approval_status="approved", approved_by="", approved_at="not-a-date"
        ),
    )
    write_document(
        tmp_path,
        "bad-date.md",
        valid_metadata(
            "REQ-004", approval_status="approved", approved_by="Person", approved_at="soon"
        ),
    )

    assert {
        "META005",
        "META006",
        "META007",
        "META008",
        "META009",
        "META010",
        "META011",
        "META012",
    } <= codes(report(tmp_path))


def test_duplicate_id_and_title_mismatch(tmp_path: Path) -> None:
    write_document(tmp_path, "one.md", valid_metadata("REQ-001"), "# Different\n")
    write_document(tmp_path, "two.md", valid_metadata("REQ-001"))

    assert {"META004", "META013", "TRACE002"} <= codes(report(tmp_path))


def test_local_links_do_not_leave_docs_and_fenced_links_are_ignored(tmp_path: Path) -> None:
    write_document(tmp_path, "target.md", valid_metadata("REQ-002"))
    write_document(
        tmp_path,
        "source.md",
        valid_metadata("REQ-001"),
        "# Example\n[Valid](target.md)\n[Missing](absent.md)\n[Outside](../outside.md)\n[External](https://example.test)\n```md\n[Ignored](also-missing.md)\n```\n",
    )

    result = report(tmp_path)

    assert {"LINK001", "LINK002"} <= codes(result)
    assert result["links"]["counts"] == {"broken": 1, "external": 1, "outside": 1, "valid": 1}  # type: ignore[index]
    assert result["links"]["external"] == [{"path": "source.md", "target": "https://example.test"}]  # type: ignore[index]


def test_traceability_detects_existing_and_unknown_identifiers(tmp_path: Path) -> None:
    write_document(tmp_path, "target.md", valid_metadata("REQ-002"))
    write_document(
        tmp_path,
        "source.md",
        valid_metadata("REQ-001"),
        "# Example\nDepends on REQ-002 and REQ-999. `REQ-998` is also visible.\n",
    )

    result = report(tmp_path)

    assert result["documents"][1]["incoming_ids"] == ["REQ-001"]  # type: ignore[index]
    assert result["traceability"]["unknown_references"] == [  # type: ignore[index]
        {"path": "source.md", "identifier": "REQ-998"},
        {"path": "source.md", "identifier": "REQ-999"},
    ]
    assert "TRACE001" in codes(result)


def test_markdown_and_json_are_deterministic_and_logically_equivalent(tmp_path: Path) -> None:
    write_document(tmp_path, "z.md", valid_metadata("REQ-002"))
    write_document(tmp_path, "a.md", valid_metadata("REQ-001"), "# Example\nREQ-002\n")

    first = report(tmp_path)
    second = report(tmp_path)

    assert json_report(first) == json_report(second)
    assert markdown_report(first) == markdown_report(second)
    assert json.loads(json_report(first))["findings"] == first["findings"]
    assert "## Human Review Required" in markdown_report(first)
    assert "### Document connections" in markdown_report(first)


def test_cli_exit_codes_strict_and_does_not_modify_source(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    source = write_document(tmp_path, "warning.md", valid_metadata(), "# Different\n")
    before = source.read_bytes()

    assert main(["--docs-dir", str(tmp_path)]) == EXIT_OK
    capsys.readouterr()
    assert main(["--docs-dir", str(tmp_path), "--strict"]) == EXIT_FINDINGS
    assert source.read_bytes() == before


def test_cli_returns_failure_for_errors_and_writes_only_outside_docs(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    (tmp_path / "bad.md").write_text("# Bad\n", encoding="utf-8")
    output = tmp_path.parent / "report.json"

    assert (
        main(["--docs-dir", str(tmp_path), "--format", "json", "--output", str(output)])
        == EXIT_FINDINGS
    )
    capsys.readouterr()
    assert json.loads(output.read_text(encoding="utf-8"))["schema_version"] == "1.0"
