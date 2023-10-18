def GetInt(promt:str):
    while 1:
        try:
            return int(input(promt))
        except ValueError:
            print ("Неправильні дані")
def GetOp(promt:str):
    while 1:
        x = str(input(promt))
        if (x != "+" and  x != "-" and x != "*" and x != "/" and x != "exit"):
            print ("Ви ввели неправильний знак")
        else:
            return x