def GetInt(promt:str):
    while 1:
        try:
            return int(input(promt))
        except ValueError:
            print ("Неправильні дані")
def GetOp(promt:str):
    return str(input(promt))