from operations import *
from functions import *
class Calculator:
    def main():
        a = Get.GetInt("Введіть перше число: ")
        b = Get.GetInt("Введіть друге число: ")
        x = Get.GetOp("Введіть знак (+ або - або * або /) (exit щоб вийти): ")
        r = Functions(a,b)
        match x:
            case "+":
                r = r.sum()
            case "-":
                r = r.minus()
            case "*":
                r = r.mult()
            case "/":
                r = r.div()
            case "exit":
                exit()
        Operations.res(a,b,x,r)
while 1:
    if __name__ == "__main__":
        Calculator.main()