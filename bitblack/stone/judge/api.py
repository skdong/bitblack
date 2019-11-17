from aip import AipNlp
from bitblack.stone import exceptions

""" 你的 APPID AK SK """
APP_ID = '17781952'
API_KEY = 'lbYGNEkReG2fl0Mh6NV1LO4j'
SECRET_KEY = 'cgXKYAlrm8nzi2nhCgdfzb4U5rEktmHh'


def get_positive(name):
    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    req = client.sentimentClassify(name)
    if "error_code" in req:
        raise exceptions.JudgeException(req["error_msg"])
    return req
