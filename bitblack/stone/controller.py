from __future__ import print_function

from pyspark.sql import SparkSession

recode_file = "space/resulte.jsonl"

spark = SparkSession.builder.appname("Get better name").getOrCreate()

sc = spark.SparkContext
nameDF = spark.read.json(recode_file)

nameDF.printSchema()
nameDF.createOrReplaceTempView("name")

spark.close()