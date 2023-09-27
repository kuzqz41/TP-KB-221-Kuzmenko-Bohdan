a = int(input ("Введіть перше число: "))
b = int(input ("Введіть друге число: "))
x = str(input("Введіть знак (+ або - або * або /): "))
match x:
    case "+":
        print ("a + b = ",a+b)
    case "-":
        print ("a - b = ",a-b)
    case "*":
        print ("a * b = ",a*b)
    case "/":
        match b:
            case 0:
                print ("Ділити на нуль не можна")
            case _:
                print ("a / b = ",a/b)
    case _:
        print ("Ви ввели неправильний знак")