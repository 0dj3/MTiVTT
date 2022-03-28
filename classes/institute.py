from main import Specialization, Group


class Institute:
    def __init__(self):
        self.specs = []
        self.groups = []

    def add_spec(self, spec: Specialization):
        if type(spec) != Specialization:
            raise Exception("Type peremennoi ne spec")
        for i in self.specs:
            if i.name == spec.getName():
                raise Exception("Takoi spec uje est`")
        self.specs.append(spec)

    def add_group(self, group: Group):
        if type(group) != Group:
            raise Exception("Type peremennoi ne group")
        for i in self.groups:
            if i == group:
                raise Exception("Takaya group uje est`")
        self.groups.append(group)