from operations import GetInt
from operations import GetOp
from functions import sum
from functions import minus
from functions import mult
from functions import div
while 1:
    try:
        a = GetInt("Введіть перше число: ")
        b = GetInt("Введіть друге число: ")
        x = GetOp("Введіть знак (+ або - або * або /) (exit щоб вийти): ")
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
    except ZeroDivisionError:
        print ("Ділити на нуль не можна")