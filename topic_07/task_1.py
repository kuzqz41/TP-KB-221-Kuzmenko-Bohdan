class Student:
    def __init__ (self, name, surname, date_of_birth):
        self.name = name
        self.surname = surname
        self. date_of_birth = date_of_birth
    def __str__(self):
        return (f"{self.name} {self.surname} {self.date_of_birth}\n")
s1 = Student("qwe", "rty", "01.01.2005")
s2 = Student("asd", "fgh", "12.12.2004")
print (s2, s1)