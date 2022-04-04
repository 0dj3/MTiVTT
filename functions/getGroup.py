from main import Group, Specialization
import pandas as pd


def importGroups():
    groups = list()
    sp = Specialization("ФИИТ")
    gr = Group(sp, 2021)
    groups.append(gr)
    sp1 = Specialization("ИВТ")
    gr1 = Group(sp1, 2017)
    groups.append(gr1)
    return groups


def getGroup(groups, name):
    if type(name) != str:
        raise Exception("type name ne str")
    listGroup = list()
    for group in groups:
        if group.name == name:
            listGroup.append(group)
    if len(listGroup) == 0:
        raise Exception("takoi group net?")
    return listGroup