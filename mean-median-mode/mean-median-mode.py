from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    mean = np.mean(x)
    median = np.median(x)
    freq = {}
    for num in x:
        freq[num] = freq.get(num ,0) + 1

    mode = x[0]
    max_freq = freq[mode]
    for num in freq:
        if freq[num] > max_freq:
            max_freq = freq[num]
            mode = num
    return {
        "mean": float(mean),
        "median": float(median),
        "mode": float(mode)
    }
        