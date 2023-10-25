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
        return "Zero Division"
def reswrite(a,b,c,d):
    file = open("topic_06\_results.txt", "a")
    file.write(f"{a} {c} {b} = {d}\n")
    file.close