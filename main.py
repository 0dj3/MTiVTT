from dataclasses import dataclass
import re

@dataclass
class Student:
    fio: str
    code: int

    # Инициализация (Проблема с чтением типа)
    def __init(self, value_fio:str, value_code:int):
        self.fio = value_fio
        self.code = value_code

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

if __name__ == "__main__":
    a = Student(34,23)
    a.setFio("Name Fio")
    a.setCode(12323)
    print(a.getCode())