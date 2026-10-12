import numpy as np

def batch_generator(X: list, y: list, batch_size: int, seed: int = 42, drop_last: bool = False):
    """
    Returns a generator of (X_batch, y_batch) tuples.
    """
    x = np.asarray(X)
    y = np.asarray(y)
    idx = np.arange(len(x))
    np.random.default_rng(seed).shuffle(idx)
    for start in range(0, len(idx), batch_size):
        batch_idx = idx[start:start + batch_size]
        if drop_last and batch_idx.size < batch_size:
            break
        yield x[batch_idx], y[batch_idx]