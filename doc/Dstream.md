# Spark Steaming

## 总览

Spark Streaming 是核心spark API的扩展，支持对在线数据流的可扩展，高通量，容错的流式处理。数据可以来自不同的源，包括Kafka，Flume，Kinesis，以及TCP socket，可以被使用高级方法如map，reduce，join，window的复杂表达式算法处理。最终，处理完的数据可以被推送到文件系统，数据库，或者在线Dashboard。实际上，你可以在数据流上应用spark machine learing 和 graph processing 

内部工作方式如下。Spark Streaming 接收在线输入数据流并把数据分批，然后spark引擎处理数据流分批后的数据。



## socket DStream

```bash
python bitblack/swall/example/send_worlds.py
spark-submit /opt/spark-2.4.4-bin-hadoop2.7/examples/src/main/python/streaming/network_wordcount.py  localhost 9999 2> spark-err.log
```

发送的数据需要"\n"结尾

output
```
-------------------------------------------
Time: 2019-11-18 09:48:09
-------------------------------------------
(u'world', 1)
(u'hello', 1)

-------------------------------------------
```