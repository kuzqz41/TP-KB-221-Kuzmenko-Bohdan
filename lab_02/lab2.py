## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}
# already sorted list



from sys import argv
import csv


list = []

def enterName():
    Name = input("Please enter student: ")
    return Name



def enterPhone():
    Phone = input("Please enter student phone: ")
    return Phone



def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["Name"] + ",  phone is " + elem["Phone"]
        print(strForPrint)
    return



def addNewElement(Name, Phone):
    newItem = {"Name": Name, "Phone": Phone}
    # find insert position
    insertPosition = 0
    for item in list:
        if Name > item["Name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return list



def deleteElement(Name):
    deletePosition = -1
    for item in list:
        if Name == item["Name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        list.pop(deletePosition)
    return list



def updateElement(Name, Phone):
    updatePosition = -1
    for item in list:
        if Name == item["Name"]:
            updatePosition = list.index(item)
            break
    if updatePosition == -1:
        print("Element was not found")
    else:
        print("Update position " + str(updatePosition))
        newItem = {"Name": Name, "Phone": Phone}
        list.pop(updatePosition)
        list.insert(updatePosition, newItem)
    return list
    # implementation required



def saveAllList(file_name):
    with open(file_name, "w", newline='') as csvfile:
        fieldnames = ["Name", "Phone"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for elem in list:
            writer.writerow({'Name': elem["Name"], 'Phone': elem["Phone"]})



def main():
    file_name = argv[1]
    with open(file_name, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            list.append({"Name":row["Name"], "Phone":row["Phone"]})
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print, S save, X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement(enterName(), enterPhone())
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement(enterName(), enterPhone())
            case "D" | "d":
                print("Element will be deleted")
                deleteElement(enterName())
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "S" | "s":
                print("List will be saved")
                saveAllList(file_name)
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")

if __name__ == "__main__":
    main()