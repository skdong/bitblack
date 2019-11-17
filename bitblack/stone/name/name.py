import random

default_len_min = 1
default_len_limit = 2


class Name:
    file_name = "statics/诗经.txt"
    end = "。"
    flags = ["。", "，", "！", "？", "：", "；"]

    def __init__(self):
        self.len_min = default_len_min
        self.len_limit = default_len_limit
        self.content = None
        self.collection = ""
        self.load()
        self.parse()

    def load(self):
        with open(self.file_name) as fp:
            self.content = fp.read()

    def parse(self):
        all_line = list()
        for line in self.content.split():
            if not line.endswith(self.end):
                last_line = line
                continue
            elif last_line:
                line = last_line + line
                last_line = None
            elif len(line) == 2:
                continue
            all_line.append(line)

        names = "".join(all_line)
        for i in names:
            if i not in self.flags:
                self.collection += i

    def get_random_name(self):
        name = ""
        for _ in range(random.randint(self.len_min, self.len_limit)):
            name += self.collection[random.randint(0, len(self.collection)-1)]
        return name


NAME = None


def get_name(len_min=1, len_limit=2):
    global NAME
    if not NAME:
        NAME = Name()
    NAME.len_min = len_min
    NAME.len_limit = len_limit
    return NAME.get_random_name()
