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


def get_surname():
    surname = Surname()
    return surname.get_random_surname()
