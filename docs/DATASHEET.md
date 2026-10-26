# Dataset datasheet - final BBO evaluation

**Dataset:** BBO initial observations and thirteen-round query history  
**Maintainer:** Beatriz Echauz (`BeatrizEchauz`)  
**Version:** CP_25 / 279 evaluations / 26 October 2026

## Motivation

I assembled this dataset to support an educational sequential black-box optimisation challenge: maximise eight unknown functions with one new evaluation per function per round. It supports surrogate fitting, query decisions, progress tracking and retrospective prediction checks.

The initial observations and evaluation portal were supplied through the Imperial College London / Emeritus programme. I generated the sequential queries and assembled their returned outputs. The underlying benchmark creators, original sampling design and dataset funding are not established by the files available here; I do not infer them from the programme branding.

## Composition

Each instance is a numerical coordinate vector and a scalar observed output belonging to one function. There are 175 supplied observations and 104 portal evaluations, for 279 pairs. Each function has 13 additional observations. Outputs include negative and extremely small values and have different scales.

| Function | Dimensions | Initial observations | Final observations | Initial best | Final best | Improvement |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 10 | 23 | 7.71087511e-16 | 7.71087511e-16 | 0 |
| 2 | 2 | 10 | 23 | 0.611205216 | 0.658239509 | 0.0470342928 |
| 3 | 3 | 15 | 28 | -0.0348353134 | -0.030963913 | 0.00387140032 |
| 4 | 4 | 30 | 43 | -4.02554228 | 0.615272937 | 4.64081522 |
| 5 | 4 | 20 | 33 | 1088.85962 | 8605.85251 | 7516.99289 |
| 6 | 5 | 20 | 33 | -0.714264948 | -0.224677015 | 0.489587932 |
| 7 | 6 | 30 | 43 | 1.3649683 | 2.6049592 | 1.2399909 |
| 8 | 8 | 40 | 53 | 9.598482 | 9.97527317 | 0.376791172 |

There are no missing outputs among these 279 evaluated pairs. Function definitions, global maxima, evaluation timestamps and initial sampling design are unavailable. The coordinate names have no verified feature-level real-world meanings in this repository. The data contains numerical benchmark observations, not identified human subjects or private communications. No credentials or course PDFs are included.

Initial inputs and outputs are `.npy` arrays. Weekly text files contain numerical lists and, in the original cumulative input file, NumPy-style array wrappers. The final `observations.csv` stores coordinates as JSON lists and labels initial observations as round 0. Historical predictions and errors are in separate files. Blank auxiliary predictions mean no auxiliary model was used; blank feedback fields at round 0 are not missing function evaluations.

## Collection process

The programme supplied initial arrays. I selected one coordinate vector per function per round and received scalar outputs from the portal. The sequence covers Modules 12-24, corresponding to rounds 1-13; Module 25 evaluates the completed history. Exact calendar dates of evaluations are not recorded, so the reliable time index is round order.

Sampling was adaptive, not a random representative survey. The workflow began with global GP-UCB search, later added local candidate pools, compared model settings and used diagnostic auxiliary models. Rounds 11 and 12 imposed an additional distance constraint for Function 5. Round 13 selected the highest predicted mean and removed that extra constraint. See [strategy evolution](STRATEGY_EVOLUTION.md) for the round-by-round record.

The `week_n` directories are cumulative prefixes. They preserve evaluation order, not original timestamps; do not concatenate them. Earlier prefixes and newly reconstructed weeks are documented as reconstructed. The supplied final cumulative input/output files are retained in `week_13/`.

## Preprocessing/cleaning/labelling

Inputs are parsed as numeric data and validated for dimensions, finite values and unit-cube bounds. Each function's cumulative feedback is appended once to its initial observations. Negative and near-zero outputs are retained; no missing outcomes are imputed and no observations are removed as outliers.

GP target normalisation occurs during fitting. Auxiliary pipelines scale inputs and targets and return predictions in original output units. Earlier classification experiments used labels based on initial-data medians; these diagnostic labels did not replace the numerical objectives. PCA was fitted separately per function to inputs only, with a standardised-input comparison; all original coordinates remained available to optimisation.

Candidate coordinates were formatted to six decimals, with later notebooks predicting on the rounded coordinates. Exported observation arrays preserve source numerical values; best-point strings are display-rounded. Raw arrays and cumulative files are retained alongside derived CSVs.

## Uses

Intended uses include educational optimisation, replaying observed progress, inspecting prediction errors and comparing modelling assumptions. A fixed historical dataset cannot establish how alternative adaptive policies would perform because their unsubmitted candidates have no observed outcomes.

Repeated local and boundary sampling overrepresents regions the search favoured. Higher-dimensional spaces remain sparse. These are sampling-policy biases, not demonstrated demographic biases. Do not use the data as a representative population sample, to assess demographic fairness, to compare raw outputs across functions, or to support safety-critical decisions without domain-specific evidence.

Users should retain provenance and round order, avoid training on future feedback when evaluating historical forecasts, and separate observed outcomes from model predictions. Independent benchmark trials would be needed to compare optimisation policies fairly.

## Distribution

I share the project at [BBO capstone](https://github.com/BeatrizEchauz/bbo-capstone). Initial arrays are in `initial_data/`, cumulative feedback in `week_1/` to `week_13/`, and final derived files in `results/final_evaluation/`. The dataset is small and does not require external large-file hosting.

The assignment requests a public repository, but the available materials do not establish a separate open-data licence for the supplied course data. Public access does not grant unrestricted reuse. Course materials and third-party libraries retain their applicable terms. See [terms and attribution](TERMS.md).

## Maintenance

I, Beatriz Echauz, maintain the repository. The optimisation phase is complete; no further queries are scheduled. Corrections should preserve raw evidence, regenerate affected summaries and be recorded in Git history and the changelog. Issues can be raised through the project repository. There is no guaranteed update schedule.

This document follows the supplied final datasheet template and expands the Module 21 documentation.
