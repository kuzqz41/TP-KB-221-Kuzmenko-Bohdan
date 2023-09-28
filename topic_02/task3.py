def sum(a,b):
    return a + b
def minus(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    return a / b
a = int(input ("Введіть перше число: "))
b = int(input ("Введіть друге число: "))
x = str(input("Введіть знак (+ або - або * або /): "))
match x:
    case "+":
        print ("a + b = ",sum(a,b))
    case "-":
        print ("a - b = ",minus(a,b))
    case "*":
        print ("a * b = ",mult(a,b))
    case "/":
        match b:
            case 0:
                print ("Ділити на нуль не можна")
            case _:
                print ("a / b = ",div(a,b))
    case _:
        print ("Ви ввели неправильний знак")