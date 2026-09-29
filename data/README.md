# Dataset Protocol — R0 Preparation

Dataset: UCI Human Activity Recognition Using Smartphones

Use case: Predict a person's current physical activity from smartphone inertial measurements.

Prediction type: Multiclass classification.

Primary metric: Macro-F1.

Secondary evidence: Accuracy and confusion matrix.

## Required Rules

- Dataset source/version must remain fixed.
- Prediction target must remain fixed.
- Train/validation/test policy must remain fixed once frozen.
- Random seeds must be recorded and remain reproducible.
- Subject-aware splitting must be used to prevent entity leakage.
- All preprocessing must be fitted on training data only.
- Validation data is used for tuning.
- Final test data remains sealed until final comparison.

## Decisions Required Before Protocol Freeze

| Decision | Status |
| --- | --- |
| Exact dataset source/version and integrity record | TBD |
| Acquisition mechanism and local file layout | TBD |
| Exact target labels and mapping | TBD |
| Input representation | TBD |
| Subject identifiers and split membership policy | TBD |
| Train/validation/test allocation, including validation ratio | TBD |
| Random seeds | TBD |
| Preprocessing method and fitted-artifact policy | TBD |
| Evaluation details and runtime measurement policy | TBD |
| Freeze date and real evidence reference | TBD |

The protocol is not yet frozen. No dataset was downloaded or modified during
setup. No split, seed, or preprocessing choice has been selected.
