from main import Subject, Specialization
from functions import getSubject
import unittest


class TestGetStudent(unittest.TestCase):

    dataSubj = getSubject.importSubjects("../../data/subject.xlsx")

    def test_one(self):  # Корректное количество строк
        self.assertEqual(len(self.dataSubj), 4)

    def test_two(self):  # Корректная проверка
        sp = Specialization("ФИИТ")
        subject = Subject("Б1.Б.22", "Основы программирования", 1, 144, sp)
        test_subj = getSubject.getSubject(self.dataSubj, "Основы программирования")[0]
        self.assertEqual(test_subj, subject)

    def test_three(self):  # Ошибка в названии дисциплины
        sp = Specialization("ФИИТ")
        subject = Subject("Б1.Б.22", "Основы программирования", 1, 144, sp)
        self.assertEqual(getSubject.getSubject(self.dataSubj, "Осноывфывфыввы программирования")[0], subject)

    def test_four(self):  # Ошибка в типе названия
        self.assertEqual(len(getSubject.getSubject(self.dataSubj, 12)), 1)

    def test_five(self):  # Ошибка в паттерне названия
        self.assertEqual(len(getSubject.getSubject(self.dataSubj, "FFFFFFASDВЫЫЫЫы")), 1)


