from main import Exam, Subject, Specialization
from datetime import date
from classes import institute
import unittest


class TestAddExam(unittest.TestCase):
    def test_one(self):  # Корректный тест
        sp = Specialization("ФИИТ")
        su = Subject("Б1.Б.22", "Основы программирования", 1, 144, sp)
        da = date(2018, 1, 10)
        ex = Exam(su, da, "2018-2019", "Эверстов Владимир Васильевич")
        inst = institute.Institute()
        inst.add_exam(ex)
        self.assertEqual(len(inst.exams), 1)

    def test_two(self):  # Ошибка при добавлении другого типа
        inst = institute.Institute()
        inst.add_exam(1)
        self.assertEqual(len(inst.exams), 1)

    def test_three(self):  # Ошибка в типе параметра specialization
        da = date(2018, 1, 10)
        ex = Exam(1, da, "2018-2019", "Эверстов Владимир Васильевич")
        inst = institute.Institute()
        inst.add_exam(ex)
        self.assertEqual(len(inst.exams), 1)

    def test_four(self):  # Ошибка в типе параметра date
        sp = Specialization("ФИИТ")
        ex = Exam(sp, 1, "2018-2019", "Эверстов Владимир Васильевич")
        inst = institute.Institute()
        inst.add_exam(ex)
        self.assertEqual(len(inst.exams), 1)

    def test_five(self):  # Ошибка в типе параметра year
        sp = Specialization("ФИИТ")
        su = Subject("Б1.Б.22", "Основы программирования", 1, 144, sp)
        da = date(2018, 1, 10)
        ex = Exam(su, da, 1, "Эверстов Владимир Васильевич")
        inst = institute.Institute()
        inst.add_exam(ex)
        self.assertEqual(len(inst.exams), 1)

    def test_six(self):  # Ошибка в типе параметра lectFio
        sp = Specialization("ФИИТ")
        su = Subject("Б1.Б.22", "Основы программирования", 1, 144, sp)
        da = date(2018, 1, 10)
        ex = Exam(su, da, "2018-2019", 1)
        inst = institute.Institute()
        inst.add_exam(ex)
        self.assertEqual(len(inst.exams), 1)

    def test_seven(self):  # Проверка на повтороный ввод (Одинаковые)
        sp = Specialization("ФИИТ")
        su = Subject("Б1.Б.22", "Основы программирования", 1, 144, sp)
        da = date(2018, 1, 10)
        ex = Exam(su, da, "2018-2019", "Эверстов Владимир Васильевич")
        inst = institute.Institute()
        inst.add_exam(ex)
        inst.add_exam(ex)
        self.assertEqual(len(inst.exams), 2)

    def test_eight(self):  # Проверка на повтороный ввод (Корректный)
        sp = Specialization("ФИИТ")
        su = Subject("Б1.Б.22", "Основы программирования", 1, 144, sp)
        sp1 = Specialization("ИВТ")
        su1 = Subject("Б1.Б.22", "Основы программирования", 1, 144, sp1)
        da = date(2018, 1, 10)
        ex = Exam(su, da, "2018-2019", "Эверстов Владимир Васильевич")
        ex1 = Exam(su1, da, "2018-2019", "Эверстов Владимир Васильевич")
        inst = institute.Institute()
        inst.add_exam(ex)
        inst.add_exam(ex1)
        self.assertEqual(len(inst.exams), 2)


if __name__ == "__main__":
    unittest.main()
