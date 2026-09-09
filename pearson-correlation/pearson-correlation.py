import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    Sigma = np.cov(X, rowvar=False)
    sigma = np.sqrt(np.diag(Sigma))
    R = np.full(Sigma.shape, np.nan, dtype=float)
    valid = sigma > 0
    R[np.ix_(valid, valid)] = (
        Sigma[np.ix_(valid, valid)] / np.outer(sigma[valid], sigma[valid])
    )
    return R