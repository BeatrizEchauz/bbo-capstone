# Model card - final BBO approach

**Name:** Per-function Gaussian Process optimisation with global and local candidate search  
**Version:** CP_24 final selection policy; CP_25 final evaluation  
**Author:** Beatriz Echauz  
**Updated:** 26 October 2026

## Model description

**Input:** Historical coordinate vectors in two, three, four, five, six or eight dimensions with scalar outputs, separately for eight functions. The candidate domain is the unit cube; portal queries use six-decimal coordinates below 1.

**Output:** A predicted mean and standard deviation for each candidate, a selection score and one proposed coordinate vector per function per round. These are forecasts and decisions, not observed function evaluations. CP_25 outputs summaries and charts only.

**Model architecture:** A separate scikit-learn GaussianProcessRegressor uses ConstantKernel × Matérn with coordinate-specific length scales plus WhiteKernel, with target normalisation. Later fits use three optimiser restarts and seed 42. Continuous parameters are re-estimated after feedback. Extra restarts were tested for Function 5 in CP_24; the original model was retained after nearly identical predictions across probes.

The final kernel smoothness is 1.5 for Functions 1-5 and 2.5 for Functions 6-8. Length-scale bounds are 0.02 to 10 for Functions 2, 4 and 8 and 0.02 to 2 otherwise. Configurations originate from CP_18's cross-validation comparison and were retained in later rounds, not repeatedly reselected by cross-validation.

Function 5 has an auxiliary MLPRegressor with one hidden layer of eight tanh units, L-BFGS solver, alpha 0.1, maximum 2,000 iterations and seed 42. Function 7 has auxiliary linear regression. Inputs and targets are scaled in these pipelines. Auxiliary predictions are diagnostic and do not supply acquisition uncertainty.

### Decision rule and evolution

Initially I used 100,000 global random candidates and UCB = mean + 2 × standard deviation. Round 5 added local search, and round 6 split the local budget into 10,000 candidates per coordinate-wise radius 0.10 and 0.03 around the incumbent. Later candidates are rounded before prediction and checked for duplicates and distance from previous observations.

CP_22 added regional diagnostics and an extra 0.01 Euclidean-distance constraint for Function 5, retained in CP_23. CP_23 used PCA to describe sampled inputs; no coordinates were removed. In CP_24, weights 0, 1 and 2 were compared on shared candidate pools. Final selection used the highest predicted mean among standard eligible candidates, removed Function 5's extra constraint and retained the general 1e-6 duplicate tolerance. A global-pool winner can still exploit predicted performance.

[Strategy evolution](STRATEGY_EVOLUTION.md) records all thirteen rounds. Classification, neural-network gradient and prompt experiments were supplementary. No Q-learning, self-play, neural acquisition ensemble or deployed service is implemented. Expected Improvement remains a possible future comparison, not a completed acquisition experiment in this workflow.

### Intended use

Educational sequential maximisation with limited evaluations and low-to-moderate dimensionality. Adaptation to real hyperparameter tuning would require suitable validation, cost accounting and domain constraints. Avoid interpreting this as a guaranteed global optimiser, an uncertainty-certified decision system or validated performance on unrelated real-world datasets.

## Performance

Performance is measured by best observed output, improvement over the initial best and number of improving rounds, separately per function. Final evaluation uses all 279 observed pairs. Historical round-13 prediction checks use forecasts recorded in CP_24 before the feedback was available; models are not refitted on those outcomes for this comparison.

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

![Best observed output](../results/final_evaluation/best_so_far.png)

Seven functions improved overall. Final-round gains occurred in Functions 5, 6, 7 and 8 after two rounds without improvement. This is evidence about the submitted points, not a controlled comparison of acquisition policies. No aggregate competition score or benchmark rank is reported.

Final absolute-error / predicted-standard-deviation ratios were approximately 0.68, 1.21, 2.23, 0.72, 1.75, 1.51, 3.55 and 1.13 for Functions 1-8. Function 7's new best coexisted with an unexpectedly large residual. Function 5's final GP absolute error was about 8.72 versus 342.58 for its auxiliary network; Function 7's GP error was about 0.134 versus 1.396 for linear regression. These are single-location diagnostics based on rounded historical predictions, not domain-wide validation or complete uncertainty calibration.

See [final prediction errors](../results/final_evaluation/round13_prediction_errors.csv) and [final outcomes](../results/final_evaluation/round13_results.csv).

## Limitations

- Only 13 added observations per function; sparse coverage is especially serious in eight dimensions.
- Adaptive sampling favours known regions and boundaries. Cross-validation on this history does not ensure accurate forecasts at new candidates.
- Matérn smoothness, stationarity and kernel bounds are modelling assumptions. Boundary warnings do not prove feature irrelevance.
- White-noise estimates can absorb model mismatch and do not establish the true observation-noise process.
- PCA explains sampled input variation, not objective importance or causal effects.
- Candidate search finds the best sampled score, not a guaranteed continuous-domain optimum.
- Function 1 remained at its initial best; near-zero outputs make ranking and model guidance difficult.
- Historical outputs come from a different execution environment; exact earlier dependency versions were not consistently captured.
- The source functions are unavailable, so unsubmitted alternatives and missing counterfactual outcomes cannot be evaluated here.

## Trade-offs

UCB exploration may buy information at the expense of immediate output. The final round reduced this information incentive by using mean-only selection, a practical horizon-aware heuristic rather than a proven optimal rule. Local search can refine a useful basin but may miss alternatives. Function 5 demonstrated that enforcing novelty can exclude a useful nearby query.

More flexible models can overfit small datasets, while simple models may miss interactions. Additional restarts diagnose numerical stability but cannot establish calibration. Keeping all PCA coordinates avoids dropping potentially useful directions at the cost of retaining the original dimensionality.

## Transparency and ethical considerations

The repository separates forecasts from outcomes, retains warnings and records negative results. It contains synthetic numerical observations, not demographic labels, so demographic fairness cannot be assessed. Real-world adaptation must account for harmful evaluations, operational limits, privacy and representative validation. Documentation supports review; it does not replace domain validation or human oversight.

See the [datasheet](DATASHEET.md), [reproduction notes](REPRODUCIBILITY.md) and [terms](TERMS.md). The structure follows the supplied final model-card template, with added intended-use and transparency sections.
