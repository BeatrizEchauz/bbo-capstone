# Reproducibility and execution

## Final evaluation

Run from the repository root with `initial_data/` and all `week_n/` folders present. Install `requirements.txt`, select that environment as the notebook kernel and execute CP_25 top to bottom. Its final evaluation needs no portal access or new GP fitting. The terminal environment and notebook kernel are separate choices.

The repository edition replaces the author's absolute Windows project paths in CP_20-CP_25 with `Path.cwd()` and uses the selected Python interpreter. This does not change the query-selection mathematics. The original uploads are the source for historical cell contents. Environment-cell outputs were cleared to avoid presenting machine-specific checks as current. Historical model outputs remain as records of the original runs.

CP_25 code cells were executed sequentially in a clean Python namespace in the packaging environment and regenerated the final CSVs and figures. This checks final analysis, not a rerun of all historical model fits. A separate Jupyter-kernel execution could not be completed in the packaging environment because socket creation was restricted; the successful validation used sequential execution of the code cells instead. `environment-validation.txt` records the actual package versions used for this check. It is not a reconstruction of the author's historical Windows environment.

## Historical rounds

CP_12 uses only initial observations. CP_13-CP_24 use their matching prior cumulative snapshot (week 1 through week 12). Never concatenate weekly cumulative snapshots. Earlier snapshots are reconstructed prefixes; they preserve order without adding future observations.

The final thirteen-round files were supplied as cumulative feedback. Their first nine prefixes were compared exactly with the repository's existing weekly files before adding weeks 10-13. The final source files retain their supplied bytes.

Early notebooks include exploratory fitting and verbose warnings. Rerunning may take longer than CP_25. Different NumPy, SciPy or scikit-learn versions can affect fitted kernels and candidate ranking. Saved outputs are historical evidence, not proof of identical new results. Seeds and configurations are in the notebook cells. Dependencies are not pinned for every historical round, and exact candidate reproduction across environments is not guaranteed.

## Independent verification

Run `python scripts/validate_data.py`. It checks initial shapes, finite values, bounds, all thirteen cumulative prefixes, final export rows and per-function best values. It also verifies the eight round-13 submitted points against recorded CP_24 predictions and checks exported historical prediction errors. This does not submit queries, infer leaderboard scores or validate hidden function formulas.

## Export conventions

`results/final_evaluation/` is authoritative for the completed project. `observations.csv` uses round 0 for initial data and JSON lists for coordinates. Raw observation values are preserved; the CSV uses 17 significant digits. `best_observed_points.csv` contains display-rounded coordinate strings. Historical prediction values are rounded to the precision saved in CP_24 and are not full-precision posterior parameters.

Existing files directly under `results/` belong to the CP_21 snapshot and remain for provenance. `presentations/` contains the Module 23 presentation, explicitly labelled historical. Neither should be mistaken for the final 13-round evaluation.
