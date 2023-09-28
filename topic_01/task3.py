import math
def discr(a,b,c):
    return b**2 - (4*a*c)
a = int (input("a: "))
b = int (input("b: "))
c = int (input("c: "))
d = discr(a,b,c)
print("d= ", d)