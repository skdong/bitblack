from __future__ import print_function

from pyspark.sql import SparkSession

recode_file = "space/resulte.jsonl"


def show_better():
    spark = SparkSession.builder.appName("Get better name").getOrCreate()

    nameDF = spark.read.json(recode_file)

    nameDF.printSchema()
    nameDF.createOrReplaceTempView("name")

    better = spark.sql(
        "select text, items[0].sentiment, items[0].positive_prob, items[0].negative_prob from name where items[0].sentiment==2  order by items[0].positive_prob desc")

    better.show(50)

    spark.close()


def main():
    show_better()


if __name__ == "__main__":
    main()
