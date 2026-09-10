import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    matrix = np.array(matrix)
    ans = np.linalg.eigvals(matrix)
    ans = np.sort(ans.real)
    return ans
    