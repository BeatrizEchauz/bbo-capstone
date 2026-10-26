> Historical technical reference notes from the Module 21 snapshot. For the final implementation and results, see [MODEL_CARD.md](MODEL_CARD.md) and [STRATEGY_EVOLUTION.md](STRATEGY_EVOLUTION.md).

# Technical foundations and design decisions

**Documentation version:** 1.1 · **Updated:** 15 October 2026

This document connects the implemented approach to established methods. The references below support the technical explanation; adding them now does not establish that each paper was consulted before earlier submissions. The notebooks and portal feedback remain the evidence of what was actually implemented and evaluated.

## Why Bayesian optimisation?

The challenge provides few observations per function and a limited sequential evaluation budget. A surrogate model estimates performance at untested inputs, while an acquisition rule decides where to evaluate next. This makes the cost of an evaluation part of the design, rather than relying only on predictive accuracy.

A separate Gaussian Process (GP) for each function provides a predictive mean and standard deviation. Rasmussen and Williams [1] provide the foundations of GP regression and covariance-based modelling. In this project, Matérn kernels express smoothness assumptions and separate length scales allow different input directions to behave differently. Those fitted scales are model parameters, not causal explanations or definitive feature-importance measurements.

## UCB and the relationship to prior research

Srinivas et al. [2] analyse GP-UCB for sequential optimisation. Their work supports combining predicted value with uncertainty when choosing an evaluation.

The implemented score is:

```text
UCB(x) = predicted_mean(x) + 2 * predicted_standard_deviation(x)
```

The fixed multiplier of 2 is a project choice. It is not a reproduction of all the assumptions or exploration schedules used in the paper's theoretical results. The finite random candidate search and fitted hyperparameters also differ from idealised analyses. Consequently, this repository does not claim the paper's regret guarantees or convergence guarantees for its submissions.

## Libraries and architectural choices

| Package | Role in the project | Reason and trade-off |
|---|---|---|
| NumPy | Numerical arrays, initial .npy files and candidate generation | Direct support for the small numerical datasets; explicit dimension checks remain necessary. |
| pandas | Comparisons, histories and exported tables | Readable tabular evidence; displayed precision must not replace full-precision selection. |
| SciPy | Numerical support and nearest-observation distance calculations | Supports the numerical workflow without introducing a separate optimisation platform. |
| scikit-learn | GP regression, kernels, linear/NN/classification baselines, scaling and CV | A consistent estimator interface fits the current small-data experiments. Custom deep-learning frameworks would add infrastructure without a demonstrated need here. |
| Matplotlib | Historical visual analysis | Supports notebook inspection; visual patterns alone do not validate a model. |
| Jupyter | Sequential experiment narrative and recorded outputs | Convenient for inspection and iteration; stateful execution is less robust than a fully modular pipeline. |

The official GaussianProcessRegressor documentation [3] describes target normalisation and optimiser restarts used in the implementation. The WhiteKernel documentation [4] clarifies the noise component. Predictive uncertainty from the fitted model must not automatically be interpreted as calibrated confidence or wholly reducible uncertainty.

PyTorch and TensorFlow were discussed in the course, but are not the training frameworks used for the current surrogates. No CNN or transformer was trained for this numerical optimisation workflow.

## Evidence guiding the design

CP_16 compared mean, linear, small neural-network and GP regressors. CP_18 compared six Matérn/bound configurations using common three-fold splits within each function. Subsequent notebooks retained selected kernel configurations and refitted their continuous parameters as feedback arrived. This is distinct from rerunning model-family selection in every round.

Global and local candidate searches provide different proposals under the same UCB rule. Auxiliary predictions for F5 and F7 expose model disagreement; they do not automatically veto or replace the GP selection. Sequential prediction errors are reviewed alongside best-so-far results because a model can improve a query while still misestimating the output or its uncertainty.

## Transparency foundations

Gebru et al. [5] motivate documenting dataset purpose, composition, collection and uses. Mitchell et al. [6] motivate reporting model intent, evaluation and limitations. These principles complement Module 21's datasheet and model-card frameworks. This repository applies them by distinguishing evaluated observations from pending proposals, documenting adaptive sampling bias, and identifying missing information rather than inventing it.

## Completed work and future improvements

| Status | Item |
|---|---|
| Implemented | GP-UCB, historical model comparisons, global/local proposals, auxiliary models, feedback error analysis and query validation. |
| Documented | Datasheet, model card, technical rationale, source mapping, results and reproduction limitations. |
| Planned | Move reusable loading, fitting and acquisition code into tested Python modules. Training is currently notebook-based. |
| Planned | Compare Expected Improvement with UCB and examine exploration-weight sensitivity under a controlled evaluation budget. |
| Planned | Assess more evenly distributed candidate designs, stricter near-repeat policies and alternative surrogates where GP errors remain large. |
| Planned | Capture a software lockfile, evaluate uncertainty over multiple rounds, and add temporal validation alongside existing CV. |

Future work should compare methods on the same data and candidate budget, report costs and failed proposals, and avoid selecting a method only because it performs well on a single favourable round. Research and software for scalable Bayesian optimisation may become useful if dimensionality or dataset size grows; no such scalability improvement is claimed here.

## References

1. Rasmussen, C. E., and Williams, C. K. I. (2006). *Gaussian Processes for Machine Learning*. MIT Press. [Author-maintained book website](https://gaussianprocess.org/gpml/).
2. Srinivas, N., Krause, A., Kakade, S. M., and Seeger, M. (2010). *Gaussian Process Optimization in the Bandit Setting: No Regret and Experimental Design*. ICML. [Author manuscript](https://arxiv.org/abs/0912.3995).
3. scikit-learn. *GaussianProcessRegressor API documentation*. [Official documentation](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html).
4. scikit-learn. *WhiteKernel API documentation*. [Official documentation](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html).
5. Gebru, T., et al. (2021; first preprint 2018). *Datasheets for Datasets*. Communications of the ACM. [Author manuscript](https://arxiv.org/abs/1803.09010).
6. Mitchell, M., et al. (2019; first preprint 2018). *Model Cards for Model Reporting*. FAT*. [Author manuscript](https://arxiv.org/abs/1810.03993).
7. Programme course materials. Module 21, *Transparency and Interpretability*: Mini-lessons 21.1 and 21.2. Course PDFs are not redistributed in this repository.

External references were checked on 15 October 2026. Online API documentation can describe a newer release than the historical notebook environment; it does not establish the original installed package versions.
