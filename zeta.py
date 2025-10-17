def fibonacci_loop(n_terms):
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]
    else:
        series = [0, 1]
        while len(series) < n_terms:
            next_term = series[-1] + series[-2]
            series.append(next_term)
        return series