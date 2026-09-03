import numpy as np
import math

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x = np.array(x)

    centered = x - np.mean(x)
    var = np.sum(centered**2) / (len(x) - 1)
    std = math.sqrt(var)

    return {
        "variance": float(var),
        "standard_deviation": float(std)
    }