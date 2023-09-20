## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", "location":"Rokossovskogo str.", "birthday":"02.11.2004"},
    {"name":"Emma", "phone":"0631234567", "location":"Shevchenko str.", "birthday":"25.06.2005"},
    {"name":"Jon",  "phone":"0631234567", "location":"Kotlyarevskogo str.", "birthday":"12.01.2005"},
    {"name":"Zak",  "phone":"0631234567", "location":"Kozatska str.", "birthday":"09.09.2004"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ",  location is " + elem["location"] + ", birthday is " + elem["birthday"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    location = input("Please enter student location: ")
    birthday = input("Please enter student birthday: ")
    newItem = {"name": name, "phone": phone, "location": location, "birthday": birthday}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        list.pop(deletePosition)
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1
    for item in list:
        if name == item["name"]:
            updatePosition = list.index(item)
            break
    if updatePosition == -1:
        print("Element was not found")
    else:
        print("Update position " + str(updatePosition))
        phone = input("Please enter student phone: ")
        location = input("Please enter student location: ")
        birthday = input("Please enter student bitrthday: ")
        newItem = {"name": name, "phone": phone, "location": location, "birthday": birthday}
        list.pop(updatePosition)
        list.insert(updatePosition, newItem)
    return
    # implementation required

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()