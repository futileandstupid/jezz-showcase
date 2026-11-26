# `jezz-showcase` — Project Instructions

## Purpose & Protected Branches
`futileandstupid/jezz-showcase` is the live Pull Request crucible demonstrating **Jezz Software Building Code (`JBC` Edition 1.3)**, **Sheet A-1/E-1 Blueprint LVS**, and **Z3 Contract Proofs** on GitHub Actions:
- **Open PR #1 (`pr/unverified-vibe-coding`):** Intentionally demonstrates a rejected unverified patch (`RED_TAG` + LVS `SHORT_CIRCUIT`).
- **Open PR #2 (`pr/certified-pce-rebate`):** Intentionally demonstrates an `OCCUPANCY_SEALED` Z3-proved **Permit-and-Contract Engineering (`PCE`)** patch.
- **Ruleset Constraints:** `preserve-showcase-pr-branches` blocks deletion and force-pushes on `refs/heads/pr/*`—never close, merge, or force-push the open showcase PRs. `main-showcase-gate` enforces `bypass_actors = []` and requires green `Enforce JBC v1.3, Blueprint LVS, Z3 Contracts, & PCE Dossier` checks on `main` (land changes to `main` via non-`pr/*` feature branches such as `chore/*` or `feat/*`).

## Compartment Architecture & Gates
- **`src/ledger_showcase/domain/`** — Closed Pydantic models (`STRICT_FROZEN_CONFIG`), `@validate_call` circuit breakers, and Z3-provable `@icontract` postconditions.
- **`src/ledger_showcase/gateway/`** — Bounded wire adapter routing strictly through `ledger_showcase.domain` perimeter exports.
- **Verification Commands:**
  - `uv run ruff check . && uv run mypy . && uv run pytest`
  - `uvx --from git+https://github.com/futileandstupid/jezz@v0.6.0 jezz inspect .`
  - `uvx --from git+https://github.com/futileandstupid/jezz@v0.6.0 jezz prove . --require-deductive`
  - `uvx --from git+https://github.com/futileandstupid/jezz@v0.6.0 jezz blueprint . --verify-target blueprint.json`
  - `uvx --from git+https://github.com/futileandstupid/jezz@v0.6.0 jezz audit dossier.json`
