from main import Student
import pandas as pd


def importStudents(file):
    data = pd.read_excel(file)
    columns = list(data.head(0).columns)
    students = list()
    for i in range(data.shape[0]):
        fio = data.get(columns[0])[i]  # ФИО
        code = data.get(columns[1])[i]  # Код
        students.append(Student(fio, int(code)))  # Добавление студента в лист
    return students


def getStudent(students, code):
    if type(code) != int:
        raise Exception("type code ne int")
    listStud = list()
    for student in students:
        if student.code == code:
            listStud.append(student)
    if len(listStud) == 0:
        raise Exception("takogo studenta net?")
    return listStud
