def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return f"Can not be divided by zero"
