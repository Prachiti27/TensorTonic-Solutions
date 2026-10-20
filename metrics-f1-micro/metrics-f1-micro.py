def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    """
    Returns the micro-averaged F1 score as a Python float rounded to four decimals.
    """
    tp = sum(
        actual == predicted for actual, predicted in zip(y_true, y_pred)
    )
    erros = len(y_true) - tp
    deno = 2 * tp + 2 * erros
    return round(2 * tp/deno,4)