import sys
from main import *
from classes import institute


def main(*args):
    inst = institute.Institute()

    if len(args[0]) > 3:
        print("Bro, otdohni. Ataxxyn suunan baran utyi :`)")
        quit()
    elif args[0][1] == 'add' and args[0][2] == "spec":
        name = input("Spec name: ")
        inst.add_spec(Specialization(name))
        print(inst.get_spec(name)[0].name)
    elif args[0][1] == 'get' and args[0][2] == "spec":
        print("Spec name: ", end="")
        #inst.add_spec(Specialization("ФИИТ"))
        name = input()
        print(inst.get_spec(name))
    elif args[0][1] == 'add' and args[0][2] == "stud":
        fio = input("FIO: ")
        code = int(input("Studka`s number: "))
        stud = Student(fio, code)
        inst.add_student(stud)
        print(inst.get_student(code)[0].fio)
    elif args[0][1] == 'get' and args[0][2] == "stud":
        print("FIO: ", end="")
        # fio = input()
        print("Studka`s number: ", end="")
        code = int(input())
        # stud = Student(fio, code)
        # inst.add_student(stud)
        print(inst.get_student(code))
    elif args[0][1] == 'add' and args[0][2] == "group":
        specName = input("Group`s spec aata: ")
        year = int(input("Group`s god: "))
        spec = Specialization(specName)  # poka mannyk buollun
        group = Group(spec, year)
        inst.add_group(group)
        print(inst.get_group(group.name)[0].name)
    elif args[0][1] == 'get' and args[0][2] == 'group':
        name = input("Group aata: ")
        print(inst.get_group(name))


if __name__ == "__main__":
    main(sys.argv)