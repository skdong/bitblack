# Python Spark

# use mysql
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