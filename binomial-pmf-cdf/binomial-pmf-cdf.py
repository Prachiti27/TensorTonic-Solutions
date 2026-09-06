import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    prob = []
    for i in range(k+1):
        x = math.comb(n,i) * p ** i * (1.0-p) ** (n-i)
        prob.append(x)

    return {
        "pmf": float(prob[k]),
        "cdf": float(sum(prob))
    }