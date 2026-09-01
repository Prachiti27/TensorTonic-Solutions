import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    ans = []
    n = len(A)
    m = len(A[0])
    for i in range(m):
        l = []
        for j in range(n):
            l.append(A[j][i])
        ans.append(l)
    return np.array(ans)
