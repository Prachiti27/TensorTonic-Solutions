def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    s = {}
    cnt = {}
    for c, t in zip(categories, targets):
        s[c] = s.get(c, 0.0) + t
        cnt[c] = cnt.get(c, 0) + 1
    means = {c: s[c]/cnt[c] for c in s}
    return [means[c] for c in categories]