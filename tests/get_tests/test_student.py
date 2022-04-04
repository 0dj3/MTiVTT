from main import Student
from functions import getStudent
import unittest


class TestGetStudent(unittest.TestCase):

    dataStud = getStudent.importStudents("../../data/students.xlsx")

    def test_one(self):  # Корректное количество строк
        self.assertEqual(len(self.dataStud), 3)

    def test_two(self):  # Корректная проверка студента
        stud = Student("Иванов Иван Иванович", 123456)
        stud1 = getStudent.getStudent(self.dataStud, 123456)[0]
        self.assertEqual(stud, stud1)

    def test_three(self):  # Ошибка в коде студента
        stud = Student("Иванов Иван Иванович", 123456)
        self.assertEqual(getStudent.getStudent(self.dataStud, 123451)[0], stud)

    def test_four(self):  # Ошибка в типе кода
        self.assertEqual(len(getStudent.getStudent(self.dataStud, "123456")), 1)

    def test_five(self):  # Ошибка в паттерне кода
        self.assertEqual(len(getStudent.getStudent(self.dataStud, 1234)), 1)


