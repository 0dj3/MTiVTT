from main import Subject, Specialization
import pandas as pd


def importSubjects(file):
    data = pd.read_excel(file)
    columns = list(data.head(0).columns)
    subjects = list()
    for i in range(data.shape[0]):
        code = data.get(columns[0])[i]  # Код
        name = data.get(columns[1])[i]  # Наименование дисциплины
        spec = Specialization(data.get(columns[2])[i])  # Направление
        sem = int(data.get(columns[3])[i])  # Семестр
        hours = int(data.get(columns[4])[i])  # Количество часов
        subjects.append(Subject(code, name, sem, hours, spec))  # Добавление дисциплины в лист
    return subjects


def getSubject(subjects, subject_name):
    if type(subject_name) != str:
        raise Exception("type name ne str")
    listSubj = list()
    for subject in subjects:
        if subject.name == subject_name:
            listSubj.append(subject)
    if len(listSubj) == 0:
        raise Exception("takogo subject net?")
    return listSubj
