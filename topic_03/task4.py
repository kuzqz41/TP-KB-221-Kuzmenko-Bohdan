def PosSearch(a,b):
    for i in range(len(a)):
        if a[i] == b:
            return i
a = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj", "kk", "ll", "mm", "nn", "oo", "pp", "qq", "rr", "ss", "tt", "uu", "vv", "ww", "xx", "yy", "zz"]
b = str(input("b: "))
a.append(b)
a.sort()
print (a)
i = PosSearch (a,b)
print ("Елемент ", b," знаходиться на ",i," позиції")