# Dataset datasheet

**Dataset:** BBO initial observations and sequential query history  
**Version:** nine completed rounds; round-10 proposals separate  
**Maintainer:** Beatriz Echauz (`BeatrizEchauz` on GitHub)  
**Documentation date:** 15 October 2026

## Motivation

The dataset supports an educational black-box optimisation challenge: maximise each of eight unknown functions using one new evaluation per function per round. It records evidence for updating surrogate models, measuring progress and auditing decisions. It is not a representative sample of a real-world population.

## Composition

There are **247 evaluated input–output pairs**: 175 supplied initial observations plus 72 evaluations from nine rounds. Eight additional proposed points are stored separately without outcomes. Each observation belongs to one function; input dimensionality ranges from two to eight. Outputs are scalar numerical values on substantially different scales, including negative and near-zero values.

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

Initial data are stored as `initial_inputs.npy` and `initial_outputs.npy` under each function directory. Cumulative `inputs.txt` files use lists of NumPy-style arrays; `outputs.txt` files contain numerical lists. Consolidated CSV records identify function, round, inputs and observed output. In `observations.csv`, round 0 denotes initial data and `inputs_json` is a JSON list of coordinates. Predictions are not substituted for observations.

Gaps include unknown function definitions and global optima, missing evaluation timestamps, unknown initial sampling design, and no round-10 feedback. Input variable names have no supplied real-world semantics. The available records contain numerical benchmark data rather than identified human subjects.

## Collection process and time frame

The programme supplied the initial observations. Subsequent coordinates were proposed in the notebooks and evaluated through the capstone portal. The recorded sequence covers nine completed submission cycles, corresponding to Modules 12–20; Module 21 prepares cycle 10. Exact start/end dates of evaluation are not documented, so round order is the reliable time index.

The strategy began with Gaussian Process predictions and random candidate search using UCB. Later rounds compared kernel bounds, auxiliary models and global versus local proposals. Current proposals maximise mean plus twice predictive standard deviation across three search proposals. Earlier strategies are recorded in the corresponding notebooks; this description does not retroactively impose the current settings on every round.

Earlier `week_n` folders in this package are reconstructed prefixes of the latest cumulative files. They preserve recorded values and temporal order rather than representing original file timestamps. Each round contributes exactly one input–output pair per function.

## Preprocessing and uses

Inputs are parsed into numeric arrays, checked for finite values and compatible dimensions, and appended to initial observations. Negative and extremely small outputs are retained. No missing outputs are imputed. GP target normalisation occurs inside fitting; auxiliary pipelines apply scaling, with predictions returned to original output units. Query coordinates are formatted to six decimals. The notebooks are authoritative for each round's transformations.

Intended uses are educational optimisation, model comparison, error analysis and reproducibility checks. Inappropriate uses include treating this adaptively selected history as an unbiased population sample, inferring demographic fairness, comparing raw output magnitude across functions, or claiming performance in safety-critical applications.

## Sampling gaps and bias

Queries depend on previous results. Repeated local searches and boundary-heavy proposals overrepresent regions the models already favour. High-dimensional regions remain sparsely explored. F5's round-10 query is only approximately 0.000235 from an existing point; passing the duplicate tolerance does not make it informative. These are search-policy biases, not evidence of demographic bias.

## Distribution and maintenance

I have made my dataset and derived CSV files available in my project repository: [BBO Capstone](https://github.com/BeatrizEchauz/bbo-capstone). I store the initial observations in `initial_data/`, cumulative feedback in `week_1/` to `week_9/`, and consolidated records in `results/`. I have not included the original course PDFs or any credentials. As explained in [Terms and attribution](TERMS.md), no independent redistribution or open-data licence was supplied with the course data.

I am responsible for maintaining the dataset. When I receive new feedback, I will preserve the raw files, validate the eight input–output pairs, add the new round, regenerate the summaries and update the documentation. I will record corrections in Git history so that previous results remain traceable. I keep round-10 proposals separate from evaluated observations until their actual portal feedback becomes available.

## Framework reference

Prepared using the categories in Module 21, Mini-lesson 21.1, Developing a datasheet: motivation, composition, collection, preprocessing/uses, distribution and maintenance.

For the supporting academic references and the distinction between implementation and planned work, see [Technical foundations](TECHNICAL_FOUNDATIONS.md).
