import jsonlines
from bitblack.swall.samples.name import name

surname = "施"

def build_name():
    return surname + name.get_name()

def build_names(num=1000):
    names = list()
    for _ in range(num):
        names.append(build_name())
    with jsonlines.open("space/names.jsonl", mode="a") as writer:
        writer.write(names)

build_names()
