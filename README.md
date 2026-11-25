# `jezz-showcase` — Live PR Crucible (`RED_TAG` Block vs. `PCE` `OCCUPANCY_SEALED`)

Companion repository for **[`futileandstupid/jezz`](https://github.com/futileandstupid/jezz)** demonstrating how **Jezz Software Building Code (`JBC` Edition 1.3)**, **Layout-vs-Schematic (`LVS`)**, and **Z3 Symbolic Contract Proofs** govern real GitHub Pull Requests.

## Inspect the Two Open Pull Requests

1. **[PR #3 — `feat: add quick SQLite fee cache lookup in gateway`](https://github.com/futileandstupid/jezz-showcase/pull/3) (*Unverified Agent PR — Blocked `RED_TAG`*)**
   - Passes `ruff`, `mypy --strict`, and `pytest` (`100%` green on traditional CI).
   - **Blocked by `futileandstupid/jezz@v0.6.0`:** Catches `JBC-SEC-001` (`LIFE_SAFETY` interpolated SQL query), `JBC-FLT-001` (`LIFE_SAFETY` silent `except sqlite3.Error: pass`), and `BlueprintGraph` `LVS` `SHORT_CIRCUIT` (`gateway -> storage` room bypass).
2. **[PR #4 — `feat(domain): add Z3-proved volume rebate calculus and sealed PCE dossier`](https://github.com/futileandstupid/jezz-showcase/pull/4) (*Certified `PCE` PR — `APPROVED`*)**
   - Passes `ruff`, `mypy --strict`, `pytest` + `Hypothesis`, `jezz inspect` (`30/30` provisions), `jezz blueprint --verify-target blueprint.json` (`LVS_CLEAN`), `jezz prove --require-deductive` (`2` Z3 `PROVED_DEDUCTIVE` obligations), and `jezz audit dossier.json` (`OCCUPANCY_SEALED`).
