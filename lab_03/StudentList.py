import csv
from Student import Student

class StudentList:
    def __init__(self, file_name):
        self.file_name = file_name
        self.list = []
        self.loadAllList()



    def printAllList(self):
        for elem in self.list:
            strForPrint = f"Student name is {elem.name}, phone is {elem.phone}"
            print(strForPrint)



    def addNewElement(self, name, phone):
        newItem = Student(name, phone)
        insertPosition = 0
        for item in self.list:
            if newItem.name > item.name:
                insertPosition += 1
            else:
                break
        self.list.insert(insertPosition, newItem)
        print("New element has been added")



    def deleteElement(self, name):
        for item in self.list:
            if name == item.name:
                self.list.remove(item)
                print("Delete student", name)
                break
        else:
            print("Element was not found")



    def updateElement(self, name, phone):
        for item in self.list:
            if name == item.name:
                item.phone = phone
                print("Update student ", name," with new phone ",phone)
                break
        else:
            print("Element was not found")
    


    def loadAllList(self):
        with open(self.file_name, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(row["Name"], row["Phone"])
                self.list.append(student)



    def saveAllList(self, file_name):
        with open(file_name, "w", newline='') as csvfile:
            fieldnames = ["Name", "Phone"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for elem in self.list:
                writer.writerow({'Name': elem.name, 'Phone': elem.phone})