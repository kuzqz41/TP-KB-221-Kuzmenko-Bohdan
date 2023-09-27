a = int(input ("Введіть перше число: "))
b = int(input ("Введіть друге число: "))
x = str(input("Введіть знак (+ або - або * або /): "))
if x=="+":
    print ("a + b = ",a+b)
elif x=="-":
    print ("a - b = ",a-b)
elif x=="*":
    print ("a * b = ",a*b)
elif x=="/":
    if b==0:
        print ("Ділити на нуль не можна")
    else:
        print ("a / b = ",a/b)
else:
    print ("Ви ввели неправильний знак")