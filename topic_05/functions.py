def sum(a,b):
    return a + b
def minus(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ділити на нуль не можна"