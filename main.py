from pydantic.dataclasses import dataclass
import re

@dataclass
class Student:
    fio: str
    code: int

    # Инициализация
    def __init__(self, value_fio:str, value_code:int):
        self.setFio(value_fio)
        self.setCode(value_code)

    # Задать ФИО
    def setFio(self, new_fio):
        # Проверка на тип
        if type(new_fio) != str:
            raise Exception("U vas wrong type")
        # Проверка введённых данных на ФИО
        pattern = '[A-ZА-ЯЁ][a-zа-яё]+\s+[A-ZА-ЯЁ][a-zа-яё]+(?:\s+[A-ZА-ЯЁ][a-zа-яё]+)?'
        if not re.fullmatch(pattern, new_fio):
            raise Exception("U vas incorrect input")
        self.fio = new_fio

    # Получить ФИО студента
    def getFio(self):
        return self.fio

    # Задать номер студента
    def setCode(self, new_code):
        # Проверка на тип
        if type(new_code) != int:
            raise Exception("U vas wrong type")
        # Проверка введённых данных на номер студента
        if not re.fullmatch(r'[0-9]{6}', str(new_code)):
            raise Exception("U vas incorrect input")
        self.code = new_code

    # Получить номер студента
    def getCode(self):
        return self.code

@dataclass
class Specialization:
    name: str

    # Инициализация
    def __init__(self, value_name:str):
        self.setName(value_name)

    # Задать название
    def setName(self, new_name):
        # Проверка типа
        if type(new_name) != str:
            raise Exception("U vas wrong type")
        # Проверка на правильность ввода названия
        if not re.fullmatch(r'([А-Я]-)?[А-Я]+-[0-9]{2}', new_name):
            raise Exception("U vas incorrect input")
        self.name = new_name

    # Получить название
    def getName(self):
        return self.name

if __name__ == "__main__":
    Specialization("М-ФИИТ-21")