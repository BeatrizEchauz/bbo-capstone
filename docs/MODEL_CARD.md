# Model card

## Overview

**Name:** Per-function Gaussian Process UCB optimisation with auxiliary diagnostics  
**Version:** CP_21, round 10 prepared (15 October 2026)  
**Developer/maintainer:** Beatriz Echauz  
**Type:** sequential Bayesian optimisation of eight numerical black-box functions  
**Implementation:** Python, NumPy, pandas, SciPy and scikit-learn; Jupyter notebooks  
**Status:** nine rounds evaluated; tenth-round results unavailable

## Intended use

This approach proposes evaluations for low-data, bounded numerical maximisation problems. It supports educational experiments and transparent allocation of a small evaluation budget. It is not validated for safety-critical decisions, arbitrary business deployment, demographic fairness assessment or guarantees of finding a global optimum. Gaussian Processes are a modelling choice, not a mandatory solution for all BBO tasks.

## Strategy and evolution

| Notebook / prepared round | Recorded development |
|---|---|
| CP_12 / 1 | Separate Matérn GPs, normalised targets, 100,000 global random candidates and UCB. |
| CP_13 / 2 | Compared original and wider length-scale bounds. |
| CP_14 / 3 | Explored above-threshold SVM classification alongside GP optimisation. |
| CP_15 / 4 | Compared regression/classification models and explored neural-network gradients and candidate steps. |
| CP_16 / 5 | Compared mean/linear/NN/GP regressors using CV; combined global/local searches and auxiliary models. |
| CP_17 / 6 | Compared global proposals with local search at 0.10 and 0.03; recorded computational costs. No CNN was trained. |
| CP_18 / 7 | Three-fold CV of six GP configurations: Matérn nu 1.5/2.5 and bounds (0.02,2), (0.02,10), (0.005,10). |
| CP_19 / 8 | Retained selected configurations; compared simple and structured prompts for interpreting the same candidates. This was not a controlled decoding experiment. |
| CP_20 / 9 | Refit continuous kernel parameters; retained GP/auxiliary structure, historical diagnostics and explicit validation. |
| CP_21 / 10 | Updated with round-9 feedback, retained configurations and documented transparency, sampling bias and limits. |

An experiment in a notebook does not imply every proposed candidate was submitted. Portal feedback is the authoritative record of evaluated coordinates. LLM assistance does not replace numerical scoring or validate unknown outputs.

## Current technical details

Each function has a `ConstantKernel * Matern + WhiteKernel` GP. Targets are normalised during fitting. Matérn nu is 1.5 for F1–F5 and 2.5 for F6–F8. Length-scale bounds are (0.02,10) for F2/F4/F8 and (0.02,2) otherwise. Continuous parameters are re-estimated by the GP optimiser, with three restarts and random state 42. Noise bounds are 1e-10 to 0.1. These configurations were retained rather than reselected by new cross-validation in CP_21.

The search samples 100,000 global and 10,000 candidates in each of two local boxes around the best observed input. Local radii are 0.10 and 0.03. The seed depends on the function (42 + function identifier). Rounded, unique candidates within the permitted bounds are screened against existing observations with the configured 1e-6 distance tolerance. The final selection uses the largest full-precision UCB = predicted mean + 2 × predictive standard deviation across the three proposals.

F5 also uses a one-hidden-layer NN with eight units; F7 uses linear regression. Their predictions are diagnostic and do not override UCB selection. Auxiliary models scale inputs and targets and return original-unit predictions. PyTorch and TensorFlow are not required by this implementation.

Round 10 selects global proposals for F1/F3, local 0.03 for F2/F4/F5/F6, and local 0.10 for F7/F8. Exact coordinates appear in `results/round_10_queries.csv`.

## Performance

The primary metric is best observed output per function; higher is better, including when all values are negative. Secondary metrics include improvement count, CV RMSE in historical comparisons, sequential prediction error, error divided by predicted standard deviation, observation distance and runtime. Unknown optima prevent calculation of true regret. Raw values should not be aggregated across the different function scales.

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

Numbers of functions improving in rounds 1–9 were **5, 2, 2, 2, 4, 3, 1, 3, 1**. Only F8 improved in round 9. There is no evidence yet about round-10 performance.

For round 9, absolute error divided by predicted standard deviation was approximately 0.20, 0.54, 0.90, 3.20, 6.36, 0.75, 0.64 and 0.89 for F1–F8. F4 and F5 illustrate substantial surrogate error. F5's auxiliary NN was closer on that evaluation, while F7's GP was closer than its auxiliary linear model. One observation cannot establish general model superiority or full uncertainty calibration. These diagnostics use rounded historical predictions.

## Assumptions and limitations

- Matérn kernels assume a form of smoothness and stationary covariance that the unknown functions may violate. F1's fitted directional length scales changed substantially between rounds, showing model sensitivity rather than established feature importance.
- Sparse, adaptively sampled data can miss narrow peaks and leave high-dimensional regions unexplored. CV on this history does not prove generalisation across the full domain.
- Eleven boundary-related fitting warnings were recorded in CP_21. Successful fitting does not prove that the bounds or model are adequate.
- Predictive standard deviation includes the fitted WhiteKernel contribution; it is not purely reducible uncertainty. High UCB can favour near-repeat points, as in F5. The white-noise component may absorb model mismatch; it does not establish stochastic portal evaluations.
- A finite random search only finds the best candidate among those tested. None of the selected round-10 means exceeds its current best observed output; optimistic UCB is not a promised improvement.
- Runtime depends on hardware and software. Exact package versions from the original environment were not captured in a reproducible lockfile, and this package has not been fully rerun end to end.

## Transparency, ethics and adaptation

Datasheets and this card expose provenance, decision rules, uncertainty and failure modes. Recording seeds, folds, warnings, candidate scores and actual feedback makes decisions auditable. Sampling bias here concerns search coverage; no demographic fairness conclusion is supported by anonymous benchmark coordinates.

Before real-world adaptation, establish variable meanings, evaluation cost, acceptable risk and domain constraints, then validate on relevant data. Avoid presenting speculative outputs as observations. Future comparisons could test other surrogate families, acquisition functions and distance policies; those are proposed improvements, not completed experiments.

More documentation is useful when it resolves a reproducibility gap: software lockfiles, evaluation timestamps and independent calibration checks would strengthen this card. Repeating tables without new evidence would not. Maintainer updates should preserve the evaluated/proposed distinction.

## Framework reference

Structured around Module 21, Mini-lesson 21.2, Analysing a model card: overview, intended use, technical details, performance, limitations and ethical considerations. Course materials are not redistributed here.

For the supporting academic references and the distinction between implementation and planned work, see [Technical foundations](TECHNICAL_FOUNDATIONS.md).
