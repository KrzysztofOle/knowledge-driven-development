# Contributing to KGAID

Thank you for improving Knowledge-Governed AI-Assisted Development (KGAID).

## Propose a change

Open an issue or pull request that states the problem, proposed outcome, affected documents, and evidence or examples. Use a focused change. Preserve historical records, including the filenames of `AUD-001` and `AUD-002`.

For a normative change, also state its compatibility impact, proposed semantic-version impact, migration implications, and dependencies. Normative changes follow `Draft → Review → Accepted → Baseline` and require explicit acceptance by the KGAID Methodology Maintainer. See [governance and release model](docs/50-governance/governance-and-release-model.md).

## Document rules

Normative documents must conform to the [metadata profile](docs/50-governance/metadata-profile.md), use `MUST`, `SHOULD`, and `MAY` in their defined sense, and keep relative links valid. Do not use KDD or Knowledge-Driven Development in normative content except in a clearly labelled historical record.

Before submitting, run:

```sh
python3 tools/check_repository.py
git diff --check
```

## Conduct and security

Follow the [Code of Conduct](CODE_OF_CONDUCT.md). Report vulnerabilities as described in [SECURITY.md](SECURITY.md), not in a public issue.
