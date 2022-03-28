from main import Specialization


class Institute:
    def __init__(self):
        self.specs = []

    def add_spec(self, spec: Specialization):
        if type(spec) != Specialization:
            raise Exception("Type peremennoi ne spec")
        for i in self.specs:
            if i.name == spec.getName():
                raise Exception("Takoi spec uje est`")
        self.specs.append(spec)
