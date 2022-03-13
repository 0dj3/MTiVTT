from main import Student
import unittest


class TestClassStudent(unittest.TestCase):
    def test_class_student(self):
        student = Student(1,1)
        student.setCode(123123)
        student.setFio("Иннокентьев Владимир")
        self.assertEqual("Иннокентьев Владимир", student.fio)
        self.assertEqual(123123, student.code)


if __name__ == '__main__':
    unittest.main()
