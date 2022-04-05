from main import Exam, Group, Specialization, Subject
from datetime import date
from functions import getExam
import unittest


class TestGetStudent(unittest.TestCase):

    def test_one(self):  # Корректное количество строк
        sp = Specialization("ФИИТ")
        group = Group(sp, 2021)
        dat = date(2018, 1, 10)
        subject = Subject("Б1.Б.22", "Основы программирования", 1, 144, sp)
        self.assertEqual(len(getExam.getExam(group.name, subject.name, dat)), 1)

    def test_two(self):  # Ошибка в типе имени группы
        ex = list()
        sp = Specialization("ФИИТ")
        dat = date(2018, 1, 10)
        subject = Subject("Б1.Б.22", "Основы программирования", 1, 144, sp)
        with self.assertRaises(Exception):
            ex = getExam.getExam(12, subject.name, dat)
        self.assertEqual(len(ex), 0)

    def test_three(self):  # Ошибка в типе имени группы
        ex = list()
        sp = Specialization("ФИИТ")
        group = Group(sp, 2021)
        dat = date(2018, 1, 10)
        with self.assertRaises(Exception):
            ex = getExam.getExam(group.name, 2, dat)
        self.assertEqual(len(ex), 0)

    def test_four(self):  # Ошибка в типе имени группы
        ex = list()
        sp = Specialization("ФИИТ")
        group = Group(sp, 2021)
        dat = "2018, 1, 10"
        subject = Subject("Б1.Б.22", "Основы программирования", 1, 144, sp)
        with self.assertRaises(Exception):
            ex = getExam.getExam(group.name, subject.name, dat)
        self.assertEqual(len(ex), 0)



