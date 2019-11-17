import random

from bitblack.stone.name import api


def generate(times=1):
    peoples = list()
    for _ in range(times):
        age = random.randint(13, 70)
        name = api.get_random_name()
        peoples.append(dict(age=age, name=name))
    return peoples
    