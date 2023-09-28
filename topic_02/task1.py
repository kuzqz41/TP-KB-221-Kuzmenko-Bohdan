import math
def discr(a,b,c):
    return b**2 - (4*a*c)
def first_root(d):
    return (-b + math.sqrt(d))/2*a
def second_root(d):
    return (-b - math.sqrt(d))/2*a
print ("Квадратне рівняння ax^2 + bx + c = 0")
a = int (input("a: "))
b = int (input("b: "))
c = int (input("c: "))
d = discr(a,b,c);
print ("d= ",d)
if d > 0:
    print ("Оскільки дискримінант більший за нуль, то рівняння має два дійсьні корені")
    x1 = first_root(d)
    x2 = second_root(d)
    print ("x1= ",x1,"   x2= ",x2)
elif d == 0:
    print ("Оскільки дискримінант дорівнює нулю, то рівняння має лише один дійсний корінь")
    x1= first_root(d);
    print ("x= ",x1)
else:
    print ("Оскільки дискримінант менший за нуль, то рівняння не має дійсних коренів")