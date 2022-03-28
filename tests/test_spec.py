from main import Specialization
from classes import institute
import unittest


class TestAddSpec(unittest.TestCase):
    def test_one(self):  # Корректный тест
        sp = Specialization("ФИИТ")
        inst = institute.Institute()
        inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 1)

    def test_two(self):  # Ошибка в типе параметра name
        sp = Specialization(12)
        inst = institute.Institute()
        inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 1)

    def test_three(self):  # Ошибка из-за пустой строки в name
        sp = Specialization("")
        inst = institute.Institute()
        inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 1)

    def test_four(self):  # Ошибка из-за пустого name
        sp = Specialization()
        inst = institute.Institute()
        inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 1)

    def test_five(self):  # Проверка на повтороный ввод (Одинаковые)
        sp = Specialization("ФИИТ")
        sp1 = Specialization("ФИИТ")
        inst = institute.Institute()
        inst.add_spec(sp)
        inst.add_spec(sp1)
        self.assertEqual(len(inst.specs), 2)

    def test_six(self):  # Проверка на повтороный ввод (Корректный)
        sp = Specialization("ФИИТ")
        sp1 = Specialization("ИВТ")
        inst = institute.Institute()
        inst.add_spec(sp)
        inst.add_spec(sp1)
        self.assertEqual(len(inst.specs), 2)


if __name__ == '__main__':
    unittest.main()
