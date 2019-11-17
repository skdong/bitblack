import jsonlines
import time

from bitblack.stone import exceptions
from bitblack.stone.name import name
from bitblack.stone.judge import api


surname = "施"
recode_file = "space/resulte.jsonl"
names = list()


def load_names():
    with open(recode_file, mode="r+", encoding="utf8") as fp:
        for item in jsonlines.Reader(fp):
            names.append(item["text"])


def write_name(name):
    with jsonlines.open(recode_file, mode="a") as fp:
        fp.write(name)


def build_name():
    new = None
    while not new and new not in names:
        new = surname + name.get_name(len_min=2, len_limit=2)
    return new


def save_name(name):
    try:
        result = api.get_positive(name)
        write_name(result)
        names.append(result["text"])
    except exceptions.JudgeException:
        time.sleep(0.5)
        save_name(name)


def build_names(num=10):
    for i in range(num):
        try:
            new = build_name()
            save_name(new)
        except Exception as err:
            print(err)


load_names()

build_names(1000)
