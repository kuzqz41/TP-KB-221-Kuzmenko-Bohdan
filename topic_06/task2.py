students = []

with open("topic_06\_students.txt") as file:
    for line in file:
        name, age = line.rstrip().split(",")
        student = {"name":name, "age": age}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"Name is {student['name']} age is {student['age']}") # braces