import math
def solve_linear(a, b):
    if a == 0:
        if b == 0:
            return f"There are infinite solutions"
        else:
            return f"There is no solution to this equation"
    x = -b / a
    return x


def solve_quadratic(a, b, c):
    if a == 0:
        return solve_linear(b, c)
    D = b**2 - (4 * a *c)
    
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return x1, x2
    elif D == 0:
        x = -b / (2 * a)
        return x
    else:
        return "There is no solution"
