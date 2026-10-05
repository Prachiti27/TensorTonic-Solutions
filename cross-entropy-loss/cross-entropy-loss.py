import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    y_true = np.asarray(y_true, dtype=int)
    y_pred = np.asarray(y_pred, dtype=float)
    row_idx = np.arange(len(y_true))
    prob = y_pred[row_idx, y_true]
    return float(-np.mean(np.log(prob)))