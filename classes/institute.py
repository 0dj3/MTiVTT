from main import Specialization, Group, Student, Exam, Subject, ExamPoints
from datetime import date


class Institute:
    def __init__(self):
        self.specs = []
        self.groups = []
        self.students = []
        self.exams = []
        self.subjects = []
        self.exam_points = []

    def add_spec(self, spec: Specialization):
        if type(spec) != Specialization:
            raise Exception("Type peremennoi ne spec")
        for i in self.specs:
            if i == spec:
                raise Exception("Takoi spec uje est`")
        self.specs.append(spec)

    def add_group(self, group: Group):
        if type(group) != Group:
            raise Exception("Type peremennoi ne group")
        for i in self.groups:
            if i == group:
                raise Exception("Takaya group uje est`")
        self.groups.append(group)

    def add_student(self, stud: Student):
        if type(stud) != Student:
            raise Exception("Type peremennoi ne student")
        for i in self.students:
            if i == stud:
                raise Exception("Takoi student uje est`")
            if i.code == stud.code:
                raise Exception("Takoi code studenta uje est`")
        self.students.append(stud)

    def add_exam(self, exam: Exam):
        if type(exam) != Exam:
            raise Exception("Type peremennoi ne exam")
        for i in self.exams:
            if i == exam:
                raise Exception("Takoi exam uje est`")
        self.exams.append(exam)

    def add_subj(self, subj: Subject):
        if type(subj) != Subject:
            raise Exception("Type peremennoi ne subject")
        for i in self.subjects:
            if i == subj:
                raise Exception("Takoi subj uje est`")
        self.subjects.append(subj)

    def add_exam_points(self, exam_points: ExamPoints):
        if type(exam_points) != ExamPoints:
            raise Exception("Type peremennoi ne exampoints")
        self.exam_points.append(exam_points)

    def get_spec(self, name):
        if type(name) != str:
            raise Exception("type name ne str")
        listSpec = list()
        for spec in self.specs:
            if spec.name == name:
                listSpec.append(spec)
        if len(listSpec) == 0:
            raise Exception("takoi spec net?")
        return listSpec

    def get_student(self, code):
        if type(code) != int:
            raise Exception("type code ne int")
        listStud = list()
        for student in self.students:
            if student.code == code:
                listStud.append(student)
        if len(listStud) == 0:
            raise Exception("takogo studenta net?")
        return listStud

    def get_subject(self, subject_name):
        if type(subject_name) != str:
            raise Exception("type name ne str")
        listSubj = list()
        for subject in self.subjects:
            if subject.name == subject_name:
                listSubj.append(subject)
        if len(listSubj) == 0:
            raise Exception("takogo subject net?")
        return listSubj

    def get_group(self, name):
        if type(name) != str:
            raise Exception("type name ne str")
        listGroup = list()
        for group in self.groups:
            if group.name == name:
                listGroup.append(group)
        if len(listGroup) == 0:
            raise Exception("takoi group net?")
        return listGroup

    def get_exam(self, gr_name, subj_name, ex_date):
        if type(gr_name) != str or type(subj_name) != str:
            raise Exception("type name ne str")
        if type(ex_date) != date:
            raise Exception("type date ne date")
        listExam = list()
        for exam in self.exams:
            if exam.group.name == gr_name and exam.subject.name == subj_name and exam.examDate == ex_date:
                listExam.append(exam)
        if len(listExam) == 0:
            raise Exception("takoi group net?")
        return listExam

    def get_exam_points(self, gr_name, subj_name, ex_date):
        if type(gr_name) != str or type(subj_name) != str:
            raise Exception("type name ne str")
        if type(ex_date) != date:
            raise Exception("type date ne date")
        listExamPoint = list()
        for exampoint in self.exam_points:
            if exampoint.groupName == gr_name and exampoint.subject.name == subj_name and exampoint.exDate == ex_date:
                listExamPoint.append(exampoint)
        if len(listExamPoint) == 0:
            raise Exception("takoi group net?")
        return listExamPoint
