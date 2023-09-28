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
if x=="+":
    print ("a + b = ", sum(a,b))
elif x=="-":
    print ("a - b = ", minus(a,b))
elif x=="*":
    print ("a * b = ", mult(a,b))
elif x=="/":
    if b==0:
        print ("Ділити на нуль не можна")
    else:
        print ("a / b = ", div(a,b))
else:
    print ("Ви ввели неправильний знак")