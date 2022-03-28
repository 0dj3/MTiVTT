from main import Specialization, Group, Student


class Institute:
    def __init__(self):
        self.specs = []
        self.groups = []
        self.students = []

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
