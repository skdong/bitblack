from aip import AipNlp
from bitblack.stone import exceptions
from bitblack.stone.name import name

""" 你的 APPID AK SK """
APP_ID = '17781952'
API_KEY = 'lbYGNEkReG2fl0Mh6NV1LO4j'
SECRET_KEY = 'cgXKYAlrm8nzi2nhCgdfzb4U5rEktmHh'


def get_client():

    return AipNlp(APP_ID, API_KEY, SECRET_KEY)


def get_positive(name):
    if not name:
        raise exceptions.NameNullException("Name is None")

    client = get_client()
    req = client.sentimentClassify(name)
    if "error_code" in req:
        raise exceptions.JudgeException(req["error_msg"])
    return req


def get_lexer():
    msg = name.Name().collection
    n = len(msg)
    client = get_client()
    import json
    with open("space/lexer1.json", mode="w", encoding="utf8") as fp:
        resulte = client.lexer(msg[:n//3])
        json.dump(resulte, fp, indent=4)
    with open("space/lexer2.json", mode="w", encoding="utf8") as fp:
        resulte = client.lexer(msg[n//3:n//3*2])
        json.dump(resulte, fp, indent=4)
    with open("space/lexer3.json", mode="w", encoding="utf8") as fp:
        resulte = client.lexer(msg[n//3*2:])
        json.dump(resulte, fp, indent=4)


def load_names():
    import json
    data = list()
    with open("space/lexer1.json", encoding="utf8") as fp:
        data = json.load(fp)
    items = list()
    for item in data["items"]:
        if len(item["item"]) == 2:
            items.append(item["item"])
    for item in set(items):
        print(item)


