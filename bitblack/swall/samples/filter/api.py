from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '17781952'
API_KEY = 'lbYGNEkReG2fl0Mh6NV1LO4j'
SECRET_KEY = 'cgXKYAlrm8nzi2nhCgdfzb4U5rEktmHh'

def get_positive(name):
    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    return client.sentimentClassify(name)
