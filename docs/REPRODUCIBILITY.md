# Reproducibility and provenance

## Sources and packaging changes

Latest supplied notebooks were mapped to CP_12–CP_21 in order. Source filenames: CP_12(4), CP_13(5), CP_14(4), CP_15(3), CP_16(1), CP_17, CP_18(1), CP_19(3), CP_20(2), CP_21 (all .ipynb).

Notebook code and stored outputs are retained except that CP_20/CP_21 setup now uses the working directory and current interpreter instead of author-specific Windows paths. This no longer verifies selection of the author's particular virtual environment. Each notebook has an explanatory archive note. Model choices, seeds and query-selection logic were not changed. Stored outputs were not regenerated during packaging; local historical paths may still appear in those outputs.

The initial .npy files were extracted unchanged from initial_data.rar. Nine-round cumulative feedback was parsed safely into literal lists. Earlier week folders were reconstructed using only the first n rounds. Derived CSVs were computed from those sources, not copied from rounded screenshots. Round-10 query strings were transcribed from the validated final selection.

## Execution and verification

Run from the repository root. Install requirements, select the notebook kernel, then run each notebook from its first cell. Earlier notebooks are exploratory archives and may need environment-specific adjustments. Their stored outputs remain useful evidence but are not proof of cross-platform execution.

Run `python scripts/validate_data.py` to check counts, finite numeric arrays, dimensions, feedback consistency, summary metrics and round-10 coordinate format. This is a data/package check, not full model re-execution. Existing historical predictions have finite displayed precision.

For exact future reruns, record Python and package versions (`python -m pip freeze`), operating system, seed, notebook commit, data snapshot, CV split definitions and candidate-generation settings. Requirements here are dependency names, not a reproduction lockfile. Optimiser and floating-point changes can alter close UCB rankings.

## Maintenance checklist

1. Preserve new portal inputs and outputs before processing.
2. Verify round count, alignment and dimensions; compare with actual submitted queries.
3. Compare prior predictions against new observations before fitting updated models.
4. Recompute performance tables and record warnings/configuration changes.
5. Update datasheet/card version and add a Git commit describing the change.
6. Keep pending proposals separate from evaluated observations.
