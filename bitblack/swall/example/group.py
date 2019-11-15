from __future__ import print_function

from pyspark.sql import SparkSession


def group_people():
    spark = SparkSession.builder.appName("PyGroup").getOrCreate()
    peoples = spark.read.json("samples/data.jsonl")
    peoples.createOrReplaceTempView("people")
    teenage = spark.sql("select name, age from people where age = 30")
    teenage.show()
    spark.stop()


def main():
    group_people()


if __name__ == "__main__":
    main()
