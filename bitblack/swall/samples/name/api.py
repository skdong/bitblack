from bitblack.swall.samples.name import surname
from bitblack.swall.samples.name import name


def get_name():
    return surname.get_surname() + name.get_name()


def get_names(num=1):
    names = []
    for _ in range(num):
        names.append(get_name())
    return names
