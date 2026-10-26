# Strategy development and observed outcomes

Rounds correspond to Modules 12-24. Model updates are not controlled causal experiments; outcomes do not isolate each change's effect.

| Round / notebook | Main development | Functions achieving a new best |
|---|---|---|
| 1 / CP_12 | Separate Matérn GPs, global random candidates, UCB weight 2 | 2, 4, 5, 7, 8 |
| 2 / CP_13 | Original versus wider length-scale bounds | 6, 8 |
| 3 / CP_14 | SVM classification diagnostics alongside continuous GP optimisation | 5, 8 |
| 4 / CP_15 | Classifier/regressor comparisons and supplementary neural-gradient candidates | 6, 8 |
| 5 / CP_16 | 100,000 global plus 20,000 local candidates; auxiliary F5 neural network and F7 linear model | 3, 4, 5, 8 |
| 6 / CP_17 | Local budget split between 0.10 and 0.03 coordinate margins | 5, 6, 7 |
| 7 / CP_18 | Cross-validation comparison of six GP configurations | 5 |
| 8 / CP_19 | Prompt-response review with Python as numerical selection reference | 4, 5, 7 |
| 9 / CP_20 | Retained GP configurations, uncertainty and auxiliary prediction review | 8 |
| 10 / CP_21 | Transparency documentation; global/local candidate comparison | 5, 7 |
| 11 / CP_22 | Neighbourhood/centroid diagnostics; extra F5 minimum distance 0.01 | None |
| 12 / CP_23 | PCA input diagnostics, all original coordinates retained; round-varying candidate seeds | None |
| 13 / CP_24 | Shared-pool weights 0/1/2; mean-only final selection; extra F5 constraint removed; fit-stability checks | 5, 6, 7, 8 |
| Final / CP_25 | Validate 13 rounds; evaluate historical forecasts; export final metrics and figures | No further queries |

Local proposals contributed successful evaluations, including Functions 4, 5 and 8 in round 5 and Function 7 in round 6. F5's near-repeat in round 10 improved the incumbent, whereas additional distance constraints in rounds 11-12 did not. F7's round-12 forecast error was about 9.96 predictive standard deviations; its final-round new best still had a residual of about 3.55 standard deviations. These observations separate optimisation progress from forecast reliability.

Future work, not implemented results: controlled Expected Improvement comparisons, sequential calibration analysis, alternative space-filling pools, fully pinned historical environments and reusable training/acquisition modules.
