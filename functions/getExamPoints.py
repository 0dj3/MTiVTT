from main import Specialization, ExamPoints, Group, Student
from datetime import date


def importExamsPoints():
    examPoints = list()
    student = Student("Иннокентьев Владимир Евгеньевич", 172531)
    spec = Specialization("ФИИТ")
    group = Group(spec, 2021)
    d = date(2021, 1, 10)
    ep = ExamPoints(student, 55.4, 30.0, d, group.name)
    examPoints.append(ep)

def getExamPoints(gr_name, subj_name, ex_date):
    if type(gr_name) != str or type(subj_name) != str:
        raise Exception("type name ne str")
    if type(ex_date) != date:
        raise Exception("type date ne date")
    listExam = list()
    listExam.append("tuox ere")
    if len(listExam) == 0:
        raise Exception("takoi group net?")
    return listExam
