# Black-box optimisation capstone

**Author:** Beatriz Echauz · **Snapshot:** 15 October 2026 · **Version:** CP_21 / round 10 prepared · **Documentation:** 1.1

This educational project maximises eight unknown functions with limited evaluations. Separate Gaussian Process surrogates rank candidate inputs by Upper Confidence Bound (UCB). Historical experiments also compare linear models, classifiers and small neural networks.

## Documentation

- [Dataset datasheet](docs/DATASHEET.md): provenance, composition, collection, uses and maintenance.
- [Model card](docs/MODEL_CARD.md): strategy, evolution, performance and limitations.
- [Reproducibility notes](docs/REPRODUCIBILITY.md): execution, source mapping and known gaps.
- [Technical foundations and references](docs/TECHNICAL_FOUNDATIONS.md).
- [Activity alignment](docs/ACTIVITY_ALIGNMENT.md).
- [GitHub upload guide](docs/GITHUB_UPLOAD_GUIDE.md).
- [Terms and attribution](docs/TERMS.md).
- [Changelog](CHANGELOG.md).

## Status and results

Nine feedback rounds have been received. Round 10 contains eight prepared queries; no round-10 outcomes are included. Preparation does not establish that portal submission occurred.

| Function | Initial observations | Current observations | Dimensions | Initial best | Best through round 9 | Improvement |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 10 | 19 | 2 | 7.7108751e-16 | 7.7108751e-16 | 0 |
| 2 | 10 | 19 | 2 | 0.61120522 | 0.65823951 | 0.047034293 |
| 3 | 15 | 24 | 3 | -0.034835313 | -0.030963913 | 0.0038714003 |
| 4 | 30 | 39 | 4 | -4.0255423 | 0.61527294 | 4.6408152 |
| 5 | 20 | 29 | 4 | 1088.8596 | 8510.2894 | 7421.4297 |
| 6 | 20 | 29 | 5 | -0.71426495 | -0.24243096 | 0.47183399 |
| 7 | 30 | 39 | 6 | 1.3649683 | 2.3747214 | 1.0097531 |
| 8 | 40 | 49 | 8 | 9.598482 | 9.9582266 | 0.35974461 |

## Repository contents

- `CP_12.ipynb`–`CP_21.ipynb`: ten chronological notebooks (rounds 1–10).
- `initial_data/function_*/`: supplied input/output NumPy arrays.
- `week_1/`–`week_9/`: cumulative feedback snapshots reconstructed from the latest nine-round files, without future rounds in earlier snapshots.
- `results/`: consolidated observations, best-so-far history, performance and pending queries.
- `scripts/validate_data.py`: independent integrity and summary checks.
- `docs/`: datasheet, model card and reproduction details.

## Run locally

Open a terminal in this repository and create/select a Python environment. Install the packages:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python scripts/validate_data.py
jupyter lab
```

Open the required notebook, select that environment's kernel, and run cells from top to bottom. Keep the working directory at the repository root. Historical notebook outputs are retained; see the reproduction notes before interpreting them as newly generated results.

The portal expects only a six-decimal coordinate string for each function. Predictions, uncertainty and UCB values are not observed outcomes. The code does not submit queries automatically.

## Implementation status

The workflow remains notebook-based. Reusable training/acquisition modules, Expected Improvement comparisons, exploration-weight experiments and a fully pinned environment are planned improvements, not completed features. The [activity alignment](docs/ACTIVITY_ALIGNMENT.md) maps requirements to current evidence.
