import csv
import pytest
from StudentList import StudentList
@pytest.fixture
def sample_file(tmpdir):
    file_path = tmpdir.join("test_students.csv")
    with open(file_path, "w", newline='') as csvfile:
        fieldnames = ["Name", "Phone"]
        list = csv.DictWriter(csvfile, fieldnames=fieldnames)
        list.writeheader()
        list.writerow({'Name': 'qwe', 'Phone': '123'})
        list.writerow({'Name': 'zxc', 'Phone': '993'})
    return str(file_path)

def test_load_all_list(sample_file):
    student_list = StudentList(sample_file)
    assert len(student_list.list) == 2
    assert student_list.list[0].name == 'qwe'
    assert student_list.list[0].phone == '123'
    assert student_list.list[1].name == 'zxc'
    assert student_list.list[1].phone == '993'

def test_add_new_element(sample_file):
    student_list = StudentList(sample_file)
    student_list.addNewElement('asd', '789')
    assert len(student_list.list) == 3
    assert student_list.list[0].name == 'asd'
    assert student_list.list[0].phone == '789'
    assert student_list.list[1].name == 'qwe'
    assert student_list.list[1].phone == '123'
    assert student_list.list[2].name == 'zxc'
    assert student_list.list[2].phone == '993'

def test_delete_element(sample_file):
    student_list = StudentList(sample_file)
    student_list.deleteElement('qwe')
    assert len(student_list.list) == 1
    assert student_list.list[0].name == 'zxc'
    assert student_list.list[0].phone == '993'

def test_update_element(sample_file):
    student_list = StudentList(sample_file)
    student_list.updateElement('zxc', '987')
    assert student_list.list[0].name == 'qwe'
    assert student_list.list[0].phone == '123'
    assert student_list.list[1].name == 'zxc'
    assert student_list.list[1].phone == '987'

def test_save_all_list(sample_file, tmpdir):
    new_file_path = str(tmpdir.join("new_test_students.csv"))
    student_list = StudentList(sample_file)
    student_list.saveAllList(new_file_path)
    with open(new_file_path, newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert len(rows) == 2
        assert rows[0]['Name'] == 'qwe'
        assert rows[0]['Phone'] == '123'
        assert rows[1]['Name'] == 'zxc'
        assert rows[1]['Phone'] == '993'
