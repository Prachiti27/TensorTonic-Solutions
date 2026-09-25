import numpy as np

def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as X.
    """
    res = np.asarray(X, dtype=float).copy()
    if res.ndim == 1:
        missing = np.isnan(res)
        obs = res[~missing]
        fill = 0.0 if obs.size == 0 else float(np.mean(obs) if strategy=="mean" else np.median(obs))
        res[missing] = fill
        return res

    for col_idx in range(res.shape[1]):
        col = res[:, col_idx]
        missing = np.isnan(col)
        obs = col[~missing]
        fill = 0.0 if obs.size == 0 else float(np.mean(obs) if strategy == "mean" else np.median(obs))
        res[missing, col_idx] = fill
    return res