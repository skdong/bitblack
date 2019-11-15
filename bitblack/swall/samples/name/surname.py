import random


class Surname:
    name = "statics/姓.txt"

    def __init__(self):
        self.content = None
        self.collection = None
        self.load()
        self.parse()

    def load(self):
        with open(self.name, encoding="utf8") as fp:
            self.content = fp.read()

    def parse(self):
        self.collection = self.content.split()

    def get_random_surname(self):
        return self.collection[random.randint(0, len(self.collection)-1)]


SURNAME = None


def get_surname():
    global SURNAME
    if not SURNAME:
        SURNAME = Surname()
    return SURNAME.get_random_surname()
