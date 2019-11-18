from __future__ import print_function

from pyspark.sql import SparkSession

recode_file = "space/resulte.jsonl"

spark = SparkSession.builder.appname("Get better name").getOrCreate()

sc = spark.SparkContext
nameDF = spark.read.json(recode_file)

nameDF.printSchema()
nameDF.createOrReplaceTempView("name")

spark.sql("select text, items[0].sentiment, items[0].positive_prob, items[0].negative_prob from name where items[0].sentiment==2  order by items[0].positive_prob desc").show(50)

spark.close()