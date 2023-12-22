from StudentList import StudentList
from sys import argv
def main():
    file_name = argv[1]
    student_list = StudentList(file_name)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, S save, X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                name = input("Please enter student: ")
                phone = input("Please enter student phone: ")
                student_list.addNewElement(name, phone)
                student_list.printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                name = input("Please enter student: ")
                phone = input("Please enter student phone: ")
                student_list.updateElement(name, phone)
            case "D" | "d":
                print("Element will be deleted")
                name = input("Please enter student: ")
                student_list.deleteElement(name)
            case "P" | "p":
                print("List will be printed")
                student_list.printAllList()
            case "S" | "s":
                print("List will be saved")
                student_list.saveAllList(file_name)
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()