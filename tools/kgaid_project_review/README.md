# KGAID Project Review

`kgaid-project-review` is an independent, offline CLI that reads an explicitly
selected documentation directory and creates a repeatable **Project Health
Report**. It inventories observable documentation facts and flags metadata,
local-link, and stable-identifier issues for a human-led review.

It is not a readiness scorer. It does not establish a baseline, approve a
document, assess content quality, or make a decision reserved for Human
Authority. It never runs Git commands, calls a network service, or changes an
analysed documentation file.

## Install

For local development from this repository:

```bash
python -m pip install -e 'tools/kgaid_project_review[dev]'
```

For a consuming project, pin a KGAID methodology tag or immutable commit:

```bash
python -m pip install 'git+https://github.com/KrzysztofOle/kgaid-methodology.git@<tag-or-commit>#subdirectory=tools/kgaid_project_review'
```

## Use

```bash
kgaid-project-review --docs-dir PATH
```

Options:

- `--output PATH` writes the report outside `--docs-dir`; without it the report
  is printed to stdout.
- `--format markdown` is the default human-readable report.
- `--format json` produces the stable machine-readable report.
- `--strict` returns failure when warnings are present as well as errors.

For example, an external project can use:

```bash
kgaid-project-review \
  --docs-dir /path/to/project/docs \
  --output project-health-report.md \
  --format markdown
```

The tool accepts relative and absolute paths and does not require a directory
named `docs`. An output target inside the analysed directory is rejected so the
review cannot add or replace analysed documentation.

## Scan boundary and exclusions

Only Markdown files (`.md` and `.markdown`) under the selected directory are
considered. The scan is recursive and read-only. Symbolic links that resolve
outside the selected directory are ignored. It skips technical directories:
`.git`, `.hg`, `.svn`, `.venv`, `venv`, `node_modules`, `__pycache__`, pytest,
mypy and Ruff caches, `build`, and `dist`.

The KGAID metadata profile excludes navigation `README.md`, `AGENTS.md`, files
under `template`/`templates`, known staging directories (`staging` and
`knowledge-staging`), and working-report directories or files ending in
`-working-report.md`. Exclusions are counted and named in the report; they are
not evidence of document quality or completeness.

Every other Markdown file is treated as a candidate KGAID-governed document.
It must comply with the executable profile in `kgaid_project_review.profile`,
which is also used by this repository's baseline controller. That profile is
the programmatic form of [KGAID Governed Document Metadata
Profile](../../docs/50-governance/metadata-profile.md).

## Findings

Findings always have a stable code, severity, path, and message. Severities are
`error`, `warning`, and `info`:

- `META001`–`META013` cover front matter, required fields, controlled values,
  title/H1 consistency, approval consistency, dates, and duplicate IDs.
- `LINK001` reports a missing local target; `LINK002` reports a local link that
  resolves outside the selected directory; `LINK003` reports an invalid local
  path. External links are inventoried only; they are never fetched.
- `TRACE001` reports an unresolved stable identifier, `TRACE002` a duplicate
  identifier, and `TRACE003` an informational candidate with no detected
  stable-identifier relationship.

The title/H1 mismatch and unresolved identifier are warnings because the tool
cannot decide their semantic intent. A document with no detected relationship
is informational, not an automatic defect.

## Metadata and traceability scope

The current KGAID profile requires `document_id`, `title`, `document_type`,
`status`, `version`, `owner`, `approval_status`, `approved_by`, and
`approved_at`. The tool validates YAML syntax (including duplicate keys), the
controlled vocabularies, numeric versions (`1`, `1.0`, or `1.0.0`), and the
approval-field rules. The title is compared with the first H1, accepting the
usual `ID — Title` heading prefix. `approved_at` is checked as ISO 8601 only
when approval is otherwise complete.

Traceability is deliberately conservative. It recognizes document references
with an upper-case identifier family and a three-or-more-digit final serial,
such as `REQ-001` and `KGAID-ARCH-014`. This avoids interpreting short labels
such as `KG-1` as document IDs. References inside fenced code blocks are
ignored. The report records incoming and outgoing identifiers, unresolved
references, duplicates, and potential orphans; it does not infer required
chains of artifact types or judge whether relationships are sufficient.

## Report formats

Markdown has fixed sections: report header, Executive Summary, Inventory,
Metadata Compliance, Approval State, Links, Traceability, Human Review
Required, and Findings. It explicitly says that no baseline or readiness
decision has been made.

JSON is a deterministic projection of the same logical data. Its top-level
keys are `schema_version`, `generated_at`, `docs_dir`, `tool_version`,
`profile`, `summary`, `inventory`, `documents`, `approval`, `links`,
`traceability`, `human_review_required`, and `findings`. User-visible lists and
mappings are sorted; the only run-time value is `generated_at`.

## Exit codes

- `0`: analysis completed without errors (and without warnings when
  `--strict` is used);
- `1`: analysis completed but found at least one error, or warnings in strict
  mode;
- `2`: invalid CLI configuration or an unavailable/unreadable documentation
  directory.

An exit code is never a statement that a project is ready, not ready, or may be
baselined. Those remain human decisions.

## Development checks

```bash
python -m pytest
python -m ruff check .
python -m ruff format --check .
```
