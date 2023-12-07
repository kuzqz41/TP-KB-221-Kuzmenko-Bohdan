from lab2 import printAllList
from lab2 import addNewElement
from lab2 import deleteElement
from lab2 import updateElement
from lab2 import saveAllList
import csv
f = open("lab2_test.csv", "w")
f.close
def test_create():
    assert addNewElement("qwe", '123') == [{'Name': 'qwe', 'Phone': '123'}]
    assert addNewElement("asd", '456') == [{'Name': 'asd', 'Phone': '456'}, {'Name': 'qwe', 'Phone': '123'}]
    assert addNewElement("zxc", '789') == [{'Name': 'asd', 'Phone': '456'}, {'Name': 'qwe', 'Phone': '123'}, {'Name': 'zxc', 'Phone': '789'}]


def test_update():
    assert updateElement("qwe", '321') == [{'Name': 'asd', 'Phone': '456'}, {'Name': 'qwe', 'Phone': '321'}, {'Name': 'zxc', 'Phone': '789'}]
    assert updateElement("asd", '654') == [{'Name': 'asd', 'Phone': '654'}, {'Name': 'qwe', 'Phone': '321'}, {'Name': 'zxc', 'Phone': '789'}]
    assert updateElement("zxc", '993') == [{'Name': 'asd', 'Phone': '654'}, {'Name': 'qwe', 'Phone': '321'}, {'Name': 'zxc', 'Phone': '993'}]

def test_delete():
    assert deleteElement("asd") == [{'Name': 'qwe', 'Phone': '321'}, {'Name': 'zxc', 'Phone': '993'}]

def test_save():
    saveAllList("lab2_test.csv")
    list = []
    with open("lab2_test.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            list.append({"Name":row["Name"], "Phone":row["Phone"]})
    assert list == [{'Name': 'qwe', 'Phone': '321'}, {'Name': 'zxc', 'Phone': '993'}]