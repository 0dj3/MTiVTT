from main import Specialization
from functions import getSpec
import unittest


class TestGetStudent(unittest.TestCase):

    dataSpec = getSpec.importSpecs()

    def test_one(self):  # Корректное количество строк
        self.assertEqual(len(self.dataSpec), 2)

    def test_two(self):  # Корректная проверка
        sp = Specialization("ФИИТ")
        group_test = getSpec.getSpec(self.dataSpec, sp.name)[0]
        self.assertEqual(group_test, sp)

    def test_three(self):  # Ошибка в названии направления
        sp = Specialization("ФИИТ")
        self.assertEqual(getSpec.getSpec(self.dataSpec, "ФЫВТ")[0], sp)

    def test_four(self):  # Ошибка в типе name
        self.assertEqual(len(getSpec.getSpec(self.dataSpec, 1)), 1)

    def test_five(self):  # Ошибка в паттерне name
        self.assertEqual(len(getSpec.getSpec(self.dataSpec, "Ффыю.Т")), 1)


