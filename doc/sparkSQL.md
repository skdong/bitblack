# Spark SQL

## work flow

create Session --> create View --> run SQL --> Show DF --> session Close

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("appname").getOrCreate()

nameDF = spark.read.json("resulte.jsonl")
nameDF.printSchema()
nameDF.createTempView("name")
better = spark.sql("select text, items[0].sentiment, items[0].positive_prob from name where items[0].sentiment==2")

spark.stop()
```