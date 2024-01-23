from pyspark.sql import SparkSession

#spark = SparkSession.builder.master("local[1]").appName("csv").getOrCreate()


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

# df = spark.read \
#         .format("jdbc") \
#         .option("url", "jdbc:oracle:thin:@//localhost:1521/freepdb1") \
#         .option("query", "select * from serial") \
#         .option("user", "scott") \
#         .option("password", "tiger") \
#         .option("driver",'oracle.jdbc.driver.OracleDriver')\
#         .load()



df7 = spark.createDataFrame(data=[(5,7,9,11),(11,13,15,19)], schema=['sno1','sno2','sno3','sno4'])

df7.write\
    .format("jdbc") \
    .mode('append') \
    .option("url", "jdbc:oracle:thin:@//localhost:1521/freepdb1") \
    .option("driver", "oracle.jdbc.driver.OracleDriver") \
    .option("dbtable", "serial_num4") \
    .option("user", "scott") \
    .option("password", "tiger") \
    .save()

df = spark.read \
        .format("jdbc") \
        .option("url", "jdbc:oracle:thin:@//localhost:1521/freepdb1") \
        .option("query", "select * from serial_num4") \
        .option("user", "scott") \
        .option("password", "tiger") \
        .option("driver",'oracle.jdbc.driver.OracleDriver')\
        .load()

df.show()


# # #
# # df.show()