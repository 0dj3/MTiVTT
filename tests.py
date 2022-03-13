from main import Student, Specialization
import unittest


class TestClass(unittest.TestCase):
    def test_class_student(self):
        student = Student("Иннокентьев Владимир", 172531)
        self.assertEqual("Иннокентьев Владимир", student.fio)
        self.assertEqual(172531, student.code)
    def test_class_specialization(self):
        spec = Specialization("М-ФИИТ-21")
        self.assertEqual("М-ФИИТ-21", spec.name)

if __name__ == '__main__':
    unittest.main()
