import pytest
@pytest.fixture()

def school_database_file():
    student_name = "tashi"
    student_location = "Boudha"
    student_gender = "male"
    student_id  = 23
    return [student_name,student_location,student_gender,student_id]

def test_1(school_database_file):
    name = "tashi"
    assert school_database_file[0] == name

def test_2(school_database_file):
    location = "swyambhu"
    assert school_database_file[1] == location

def test_3(school_database_file):
    gender = "male"
    assert school_database_file[2] == gender

def test_4(school_database_file):
    id = 23
    assert school_database_file[3] == id