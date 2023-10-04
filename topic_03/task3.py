a={'qwe':123}
b={'asd':456}
c={'qwe':123,'asd':456}
a.update(b)
print ("update - ",a)
del(b)
a.clear()
print("clear - ",a)
x=c.keys()
print ("keys - ",x)
x=c.values()
print ("values - ",x)
x=c.items()
print("items - ",x)