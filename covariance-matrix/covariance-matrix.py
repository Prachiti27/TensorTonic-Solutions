import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    m = np.mean(X, axis=0)
    Xc = []
    n = len(X)
    for i in range(n):
        Xc.append(X[i] - m)
    Xc = np.array(Xc)
    Xct = Xc.T

    ans = np.dot(Xct, Xc)/(n-1)
    return ans