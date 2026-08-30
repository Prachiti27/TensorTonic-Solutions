import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    n = len(x)
    ans = 0.0
    for i in range(n):
        ans += (x[i]*y[i])
    return ans