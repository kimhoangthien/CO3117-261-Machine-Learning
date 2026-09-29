# CO3117 Machine Learning – Individual Longitudinal Assignment

One dataset, one use case, many models.

The dataset and prediction problem remain fixed throughout the semester.
Different model families will later be evaluated under a common experimental protocol.
This repository is organized to hold longitudinal evidence: first attempts, later
corrections, experiments, written exercises, and weekly learning records. Those
artifacts are not yet present; this is the R0 preparation skeleton.

## Dataset

UCI Human Activity Recognition Using Smartphones.
Source/version and acquisition details: TBD in [the dataset protocol](data/README.md).

## Use Case

Predict a person's current physical activity from smartphone inertial measurements.

## Experimental Protocol

Multiclass classification with Macro-F1 as the primary metric; accuracy and a
confusion matrix provide secondary evidence. Subject-aware splitting and
training-only preprocessing are required. Split policy, seeds, representation,
and preprocessing choices are TBD until R0 protocol freeze.

## Repository Structure

- Root Markdown files: progress, model and AI-use logs, references, submission checklists.
- `data/`: dataset protocol.
- `docs/`: navigation, PRE-RELEASE catch-up skeleton, future weekly learning posts.
- `exercises/`, `exam/`: future student-authored drills and exam preparation.
- `src/`: data/metrics stubs, future `from_scratch/` and `reference_adapters/` code.
- `experiments/`: `part1_pre_midterm/` and `part2_post_midterm/` workspaces.
- `tests/`: future checks.
- `results/`: header-only metrics CSV and future `figures/`.
- `report/`: future submission reports.

## Setup

Use Python with a virtual environment and `requirements.txt`. From the repository
root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Dependencies are unpinned; a validated Python/dependency version record is TBD.
These are setup instructions, not a claim that the environment has been installed
or verified. Dataset acquisition is TBD; this setup does not download data.

## Current Progress

R0 preparation skeleton only. No models are implemented and the protocol is not
yet frozen. Next: R0 protocol freeze and student-authored W01–W03 work.
See [progress](PROGRESS.md) and [documentation navigation](docs/index.md).
