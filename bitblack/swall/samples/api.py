import pymysql
import jsonlines

from bitblack.swall.samples import people
from bitblack.swall.samples import config


def json_data():
    with jsonlines.open("samples/data.jsonl", mode="w") as fp:
        fp.write(people.generate(1000000))


def json_datas(n=5):
    for i in range(5):
        with jsonlines.open("samples/data_"+str(i)+".jsonl", mode="w") as fp:
            fp.write(people.generate(100000))


def get_mysql_data():
    db = pymysql.connect(**config.CONFIG)
    cursor = db.cursor()
    sql = "create database test"
    cursor.executs(sql)
    db.commit()
    db.close()


json_datas()
