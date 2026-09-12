import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    x = np.asarray(x, dtype=float)
    n = x.size
    mean = np.mean(x)
    centered= x  - mean
    s = np.sqrt(np.sum(centered**2) / (n - 1))
    if s == 0.0:
        diff = float(mean - mu0)
        if diff == 0.0:
            return 0.0
        return float(np.inf if diff > 0 else -np.inf)
    return float((mean - mu0) / (s/np.sqrt(n)))