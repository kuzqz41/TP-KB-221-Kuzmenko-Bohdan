class Functions:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sum(self):
        return self.a + self.b
    def minus(self):
        return self.a - self.b
    def mult(self):
        return self.a * self.b
    def div(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return "Zero Division"
class Result:
    def reswr(a,b,c,d):
        file = open("topic_07\_results.txt", "a")
        file.write(f"{a} {c} {b} = {d}\n")
        file.close