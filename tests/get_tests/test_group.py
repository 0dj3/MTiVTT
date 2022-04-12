from main import Group, Specialization
from functions import getGroup
import unittest


class TestGetStudent(unittest.TestCase):

    dataGroup = getGroup.importGroups()

    def test_one(self):  # Корректное количество строк
        self.assertEqual(len(self.dataGroup), 2)

    def test_two(self):  # Корректная проверка группы
        sp = Specialization("ФИИТ")
        group = Group(sp, 2021)
        group_test = getGroup.getGroup(self.dataGroup, group.name)[0]
        self.assertEqual(group_test.name, group.name)


    def test_three(self):  # Ошибка в названии группы
        sp = Specialization("ФИИТ")
        group = Group(sp, 2021)
        self.assertEqual(getGroup.getGroup(self.dataGroup, "ФИИТ-17")[0], group)

    def test_four(self):  # Ошибка в типе name
        self.assertEqual(len(getGroup.getGroup(self.dataGroup, 1)), 1)

    def test_five(self):  # Ошибка в паттерне name
        self.assertEqual(len(getGroup.getGroup(self.dataGroup, "ФИИТ")), 1)


