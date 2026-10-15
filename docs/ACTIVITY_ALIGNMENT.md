# Alignment with capstone activities

This map links the supplied activity requirements to repository evidence. It checks the requirements and recorded implementation, not the exact wording of every previously published discussion response.

| Activity | Requirement | Evidence | Status or qualification |
|---|---|---|---|
| 16.2 | Explain repository structure and improvements | README; REPRODUCIBILITY.md | Organised data, chronological notebooks, results, scripts and documents. Model code is still notebook-based. |
| 16.2 | Justify libraries | TECHNICAL_FOUNDATIONS.md | Explains roles and trade-offs; no claim that PyTorch/TensorFlow trained these models. |
| 16.2 | Describe purpose, inputs, outputs and objectives | README; DATASHEET.md | Eight maximisation tasks; evaluated pairs distinguished from proposals. |
| 17.2 | Ground the approach in prior work | TECHNICAL_FOUNDATIONS.md | GP and GP-UCB references linked to implementation, with limits on theoretical claims. |
| 17.2 | Explain papers and software choices | TECHNICAL_FOUNDATIONS.md | References added for technical grounding; no invented historical reading claims. |
| 17.2 | Document future refinements | TECHNICAL_FOUNDATIONS.md | Planned changes are explicitly labelled. |
| 21.2 | Dataset motivation | DATASHEET.md / Motivation | Educational optimisation and decision auditing. |
| 21.2 | Dataset composition and gaps | DATASHEET.md / Composition | 247 evaluated observations; dimensions, formats and missing information. |
| 21.2 | Collection and time frame | DATASHEET.md / Collection process and time frame | Nine completed cycles, initial data provenance and unavailable timestamps. |
| 21.2 | Preprocessing and uses | DATASHEET.md / Preprocessing and uses | Transformations, intended uses and inappropriate uses. |
| 21.2 | Distribution and maintenance | DATASHEET.md; TERMS.md | Maintainer, distribution status, rights limitations and update process. |
| 21.2 | Model name, type and version | MODEL_CARD.md / Overview | CP_21, round 10 prepared. |
| 21.2 | Intended and excluded uses | MODEL_CARD.md / Intended use | Scope and out-of-scope applications. |
| 21.2 | Evolution across rounds | MODEL_CARD.md / Strategy and evolution | Ten notebooks, with only nine feedback rounds available. |
| 21.2 | Performance and metrics | MODEL_CARD.md / Performance; results/ | Per-function best values, improvement history and error diagnostics. |
| 21.2 | Assumptions and failure modes | MODEL_CARD.md / Assumptions and limitations | Smoothness, sampling gaps, uncertainty, warnings and near repeats. |
| 21.2 | Ethics, transparency and adaptation | MODEL_CARD.md / Transparency, ethics and adaptation | Auditability, appropriate use and reproducibility gaps. |
| 21.2 | Public upload and README links | README; GITHUB_UPLOAD_GUIDE.md | Links prepared. Publication and discussion-board submission remain user actions until confirmed. |

## Relationship to first-round plans

The first-round reflection proposed wider kernel bounds, comparison with Expected Improvement, exploration-weight review, more evenly distributed candidates and local refinement. Later notebooks document wider-bound comparisons and local proposals. This package does not claim that Expected Improvement, systematic exploration-weight tuning or space-filling candidate methods were completed; they remain future work.

## Delivery checklist

- [x] Datasheet and model card prepared in English.
- [x] README links to both documents and the technical foundations.
- [x] Historical observations and pending queries kept separate.
- [x] Data validation and local documentation-link checks completed.
- [ ] Public repository uploaded and its links checked online.
- [ ] Repository URL submitted on the discussion board.
- [ ] Thoughtful feedback posted on peers' work.
