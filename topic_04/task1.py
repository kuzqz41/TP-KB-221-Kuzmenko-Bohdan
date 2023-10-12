def sum(a,b):
    return a + b
def minus(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    return a / b
def GetInt(promt:str):
    while 1:
        try:
            return int(input(promt))
        except ValueError:
            print ("Неправильні дані")
while 1:
    a = GetInt("Введіть перше число: ")
    b = GetInt("Введіть друге чисол: ")
    x = str(input("Введіть знак (+ або - або * або /) (exit щоб вийти): "))
    match x:
        case "+":
            print ("a + b = ",sum(a,b))
        case "-":
            print ("a - b = ",minus(a,b))
        case "*":
            print ("a * b = ",mult(a,b))
        case "/":
            print ("a / b = ",div(a,b))
        case "exit":
            break
        case _:
            print ("Ви ввели неправильний знак")