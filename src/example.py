def is_positive_pair(a, b):
    return a > 0 and b > 0


def calc(a, b):
    x = 0
    if is_positive_pair(a, b):
        x = abs(a - b)
    return x
