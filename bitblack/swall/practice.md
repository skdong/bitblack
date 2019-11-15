# Python Spark

## use mysql

```bash
pyspark --jars /opt/spark-2.4.4-bin-hadoop2.7/jars/mysql-connector-java-8.0.18/mysql-connector-java-8.0.18.jar --driver-class-path /opt/spark-2.4.4-bin-hadoop2.7/jars/mysql-connector-java-8.0.18/mysql-connector-java-8.0.18.jar
```

```python
# Creates a DataFrame based on a table named "people"
# stored in a MySQL database.
url = \
  "jdbc:mysql://172.21.0.2:3306/test?user=straw;password=123456"
df = sqlContext \
  .read \
  .format("jdbc") \
  .option("url", url) \
  .option("dbtable", "people") \
  .load()

# Looks the schema of this DataFrame.
df.printSchema()
```

```python
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName("test").setMaster("spark://10.0.25.9:7077")
sc = SparkContext(conf=conf)

data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)
distData.reduce(lambda a, b: a + b)

val textFile = sc.textFile("file:///opt/spark-2.4.4-bin-hadoop2.7/README.md")
```

spark 读取的json文件为jsonlines格式

官方例子在examples\src\main\python\sql\datasource.py