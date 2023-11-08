from functions import *
class Get:
    def GetInt(promt):
        while 1:
            try:
                return int(input(promt))
            except ValueError:
                print ("Неправильні дані")
    def GetOp(promt):
        while 1:
            x = str(input(promt))
            if (x != "+" and  x != "-" and x != "*" and x != "/" and x != "exit"):
                print ("Ви ввели неправильний знак")
            else:
                return x
class Operations:
    def res(a,b,c,d):
        print (f"{a} {c} {b} = {d}")
        Result.reswr(a,b,c,d)