from main import Specialization


def importSpecs():
    specs = list()
    sp = Specialization("ФИИТ")
    specs.append(sp)
    sp1 = Specialization("ИВТ")
    specs.append(sp1)
    return specs


def getSpec(specs, name):
    if type(name) != str:
        raise Exception("type name ne str")
    listSpec = list()
    for spec in specs:
        if spec.name == name:
            listSpec.append(spec)
    if len(listSpec) == 0:
        raise Exception("takoi spec net?")
    return listSpec
