class Student:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return repr((self.name, self.age))
students = [
    Student("Fink", 57),
    Student("Ihor", 37),
    Student("Jon", 44),
    Student("Zak", 27),
]
print (sorted(students, key=lambda student: student.age))