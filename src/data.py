"""R0 data protocol placeholders; no loader or preprocessing is implemented.

Dataset: UCI Human Activity Recognition Using Smartphones.
Split policy, seeds, representation, and preprocessing remain undecided.
Function signatures are provisional until the protocol is frozen.
"""


def load_raw_data(*args, **kwargs):
    """TODO: Load the fixed dataset after source/version and files are agreed."""
    raise NotImplementedError("Dataset acquisition and file layout are TBD.")


def create_subject_aware_split(*args, **kwargs):
    """TODO: Split by subject using the approved policy and recorded seeds."""
    raise NotImplementedError("Subject split policy, ratios, and seeds are TBD.")


def fit_preprocessing(*args, **kwargs):
    """TODO: Fit the approved preprocessing on training data only."""
    raise NotImplementedError("Preprocessing method is TBD.")


def transform_data(*args, **kwargs):
    """TODO: Apply training-fitted preprocessing without refitting."""
    raise NotImplementedError("Preprocessing and its fitted artifact are TBD.")


def get_train_validation_test(*args, **kwargs):
    """TODO: Prepare frozen splits; preserve the sealed final-test boundary.

    Validation is for tuning. Test access must remain sealed until final comparison.
    """
    raise NotImplementedError("R0 protocol freeze and test-access policy are TBD.")
