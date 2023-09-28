import math
def discr(a,b,c):
    return b**2 - (4*a*c)
def roots(a,b,c):
    d = discr(a,b,c)
    if d > 0:
        x1 = (-b + math.sqrt(d))/2*a
        x2 = (-b - math.sqrt(d))/2*a
    elif d == 0:
        x1 = (-b + math.sqrt(d))/2*a
        x2 = "Кореня не існує"
    else:
        x1 = "Кореня не існує"
        x2 = "Кореня не існує"
    return x1, x2
print ("Квадратне рівняння ax^2 + bx + c = 0")
a = int (input("a: "))
b = int (input("b: "))
c = int (input("c: "))
d = discr(a,b,c);
print ("d= ",d)
x1, x2 = roots(a,b,c)
print ("x1= ",x1,"      x2= ",x2)