import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    X = np.asarray(X, dtype=float)
    n, d = X.shape
    mean = X.mean(axis=0)
    x_c = X - mean
    cov = (x_c.T @ x_c) / (n-1)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, idx]
    w = eigenvectors[:,:k]
    for j in range(k):
        max_idx = np.argmax(np.abs(w[:,j]))
        if w[max_idx, j] < 0:
            w[:, j] *= -1
    x_proj = x_c @ w
    return x_proj.tolist()