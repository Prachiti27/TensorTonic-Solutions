import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    matrix = np.asarray(A, dtype=float)
    size = matrix.shape[0]
    augmented = np.concatenate((matrix.copy(), np.eye(size)), axis=1)
    for col in  range(size):
        pivot = col + np.argmax(np.abs(augmented[col:, col]))
        if abs(augmented[pivot, col]) < 1e-12:
            return None
        augmented[[col, pivot]] = augmented[[pivot,col]]
        augmented[col] /= augmented[col, col]
        for row in range(size):
            if row != col:
                augmented[row] -= augmented[row, col] * augmented[col]
    return augmented[:, size:]