import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    y = np.asarray(y, dtype=int)
    if len(y) == 0:
        return 0.0

    _, cnt = np.unique(y, return_counts=True)
    prob = cnt / len(y)
    return float(-np.sum(prob * np.log2(prob)))