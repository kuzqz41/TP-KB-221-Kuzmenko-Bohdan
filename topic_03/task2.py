a=[1,2,3]
b=[6,2,5]
c=[]
d=[]
a.extend(b)
print ("extend - ",a)
c.append(1)
c.append(9)
print ("append - ",c)
a.insert(2, "qwe")
print ("insert - ",a)
a.remove (3)
print ("remove - ",a)
a.clear()
print ("clear - ",a)
b.sort()
print("sort - ",b)
b.reverse()
print("reverse - ",b)
d = b.copy()
print("copy - ",d)