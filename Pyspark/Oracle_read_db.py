from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]").appName("csv").getOrCreate()


#from Utility_functions.Common_libraries import * #get_dataset, count_validation,read_file, read_cosmos, read_db, duplicate


from pyspark.sql import SparkSession
import pandas as pd
import json

#jar_path='/Users/harish/Downloads/spark-3.4.1-bin-hadoop3/jars/sqljdbc4-2.0.jar'
spark = SparkSession.builder.master("local")\
    .appName("test") \
    .config("spark.jars","/Users/harish/Downloads/spark-3.4.1-bin-hadoop3/jars/ojdbc8-21.5.0.0.jar")\
    .config("spark.driver.extraClassPath","/Users/harish/Downloads/spark-3.4.1-bin-hadoop3/jars/ojdbc8-21.5.0.0.jar") \
    .config("spark.executor.extraClassPath","/Users/harish/Downloads/spark-3.4.1-bin-hadoop3/jars/ojdbc8-21.5.0.0.jar") \
    .getOrCreate()

df = spark.read \
        .format("jdbc") \
        .option("url", "jdbc:oracle:thin:@//localhost:1521/freepdb1") \
        .option("query", "select * from serial") \
        .option("user", "scott") \
        .option("password", "tiger") \
        .option("driver",'oracle.jdbc.driver.OracleDriver')\
        .load()


df.show()

df7 = spark.createDataFrame(data=[(145,3,3242),(242,92,31)], schema=['c1','c2','c3'])

df7.write\
    .format("jdbc") \
    .mode('append') \
    .option("url", "jdbc:oracle:thin:@//localhost:1521/freepdb1") \
    .option("driver", "oracle.jdbc.driver.OracleDriver") \
    .option("dbtable", "test6") \
    .option("user", "scott") \
    .option("password", "tiger") \
    .save()


# # #
# # df.show()