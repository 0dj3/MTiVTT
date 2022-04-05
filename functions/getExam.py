from main import Exam, Specialization, Subject
from datetime import date


def importExams():
    exams = list()
    spec = Specialization("ФИИТ")
    subject = Subject("Б1.Б.22", "Основы программирования", 1, 144, spec)
    d = date(2018, 1, 10)
    exam = Exam(subject, d, "2018-2019", "Эверстов Владимир Васильевич")
    exams.append(exam)
    spec1 = Specialization("ИВТ")
    subject1 = Subject("Б1.Б.22", "Основы программирования", 1, 144, spec1)
    d1 = date(2018, 1, 10)
    exam1 = Exam(subject1, d1, "2018-2019", "Эверстов Владимир Васильевич")
    exams.append(exam1)

def getExam(gr_name, subj_name, ex_date):
    if type(gr_name) != str or type(subj_name) != str:
        raise Exception("type name ne str")
    if type(ex_date) != date:
        raise Exception("type date ne date")
    listExam = list()
    listExam.append("tuox ere")
    if len(listExam) == 0:
        raise Exception("takoi group net?")
    return listExam
