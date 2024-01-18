from pyspark.sql import SparkSession

#from Utility_functions.Common_libraries import * #get_dataset, count_validation,read_file, read_cosmos, read_db, duplicate

from pyspark.sql import SparkSession
import pandas as pd
import json
#jar_path='/Users/harish/Downloads/spark-3.4.1-bin-hadoop3/jars/sqljdbc4-2.0.jar'
spark = SparkSession.builder.master("local")\
    .appName("test") \
    .config("spark.jars",r"C:\Users\Chiranjeevi\Desktop\spark-3.5.0-bin-hadoop3\jars\ojdbc8-21.5.0.0.jar")\
    .config("spark.driver.extraClassPath",r"C:\Users\Chiranjeevi\Desktop\spark-3.5.0-bin-hadoop3\jars\ojdbc8-21.5.0.0.jar") \
    .config("spark.executor.extraClassPath",r"C:\Users\Chiranjeevi\Desktop\spark-3.5.0-bin-hadoop3\jars\ojdbc8-21.5.0.0.jar") \
    .getOrCreate()
df = spark.read \
        .format("jdbc") \
        .option("url", "jdbc:oracle:thin:@//localhost:1521/ORCL") \
        .option("query", "select * from emp") \
        .option("user", "scott") \
        .option("password", "tiger") \
        .option("driver",'oracle.jdbc.driver.OracleDriver')\
        .load()

df.show()

# df.write.mode("overwrite") \
#     .format("jdbc") \
#     .option("url", "jdbc:oracle:thin:@//localhost:1521/freepdb1") \
#     .option("driver", "oracle.jdbc.driver.OracleDriver") \
#     .option("dbtable", "serial") \
#     .option("user", "scott") \
#     .option("password", "tiger") \
#     .save()
# # #
# # df.show()