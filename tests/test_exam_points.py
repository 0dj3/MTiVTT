from main import ExamPoints, Student
from classes import institute
import unittest


class TestAddExamPoints(unittest.TestCase):
    def test_one(self):  # Корректный тест
        student = Student("Иннокентьев Владимир Евгеньевич", 172531)
        ep = ExamPoints(student, 55.4, 30.0)
        inst = institute.Institute()
        inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 1)

    def test_two(self):  # Ошибка в типе параметра student
        ep = ExamPoints(1, 55.4, 30.0)
        inst = institute.Institute()
        inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 1)

    def test_three(self):  # Ошибка в типе параметра inpoints
        student = Student("Иннокентьев Владимир Евгеньевич", 172531)
        ep = ExamPoints(student, 55, 30.0)
        inst = institute.Institute()
        inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 1)

    def test_four(self):  # Ошибка в типе параметра exampoints
        student = Student("Иннокентьев Владимир Евгеньевич", 172531)
        ep = ExamPoints(student, 55.4, 30)
        inst = institute.Institute()
        inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 1)

    def test_five(self):  # Ошибка в количестве баллов параметра inpoints > 70
        student = Student("Иннокентьев Владимир Евгеньевич", 172531)
        ep = ExamPoints(student, 80.2, 30.0)
        inst = institute.Institute()
        inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 1)

    def test_six(self):  # Ошибка в количестве баллов параметра inpoints < 0
        student = Student("Иннокентьев Владимир Евгеньевич", 172531)
        ep = ExamPoints(student, -55.4, 30.0)
        inst = institute.Institute()
        inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 1)

    def test_seven(self):  # Ошибка в количестве баллов параметра exampoints < 0
        student = Student("Иннокентьев Владимир Евгеньевич", 172531)
        ep = ExamPoints(student, 55.4, -30.0)
        inst = institute.Institute()
        inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 1)

    def test_eight(self):  # Ошибка в количестве баллов параметра exampoints > 30
        student = Student("Иннокентьев Владимир Евгеньевич", 172531)
        ep = ExamPoints(student, 55.4, 31.0)
        inst = institute.Institute()
        inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 1)

    def test_nine(self):  # Проверка на повтороный ввод
        student = Student("Иннокентьев Владимир Евгеньевич", 172531)
        ep = ExamPoints(student, 55.4, 30.0)
        inst = institute.Institute()
        inst.add_exam_points(ep)
        inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 2)


if __name__ == "__main__":
    unittest.main()
