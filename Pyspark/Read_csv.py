
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]").appName("csv").getOrCreate()

# df_csv= spark.read.csv("/Users/harish/PycharmProjects/pythonProject/source_files/Contact_info.csv")
#
# df_csv.show()
#
# print(df_csv.count())
#
# df_csv.printSchema()
# print("#"*40)
# df_csv2 = spark.read.option("header", True).csv("/Users/harish/PycharmProjects/pythonProject/source_files/Contact_info.csv")
#
# df_csv2.show()
#
# print(df_csv2.count())
#
# df_csv2.printSchema()
#
# print("#"*40)
# df_csv3 = (spark.read.option("header", True).
#             option("inferSchema", True).
#            csv("/Users/harish/PycharmProjects/pythonProject/source_files/Contact_info.csv"))
#
# df_csv3.show()
#
# print(df_csv3.count())
#
# df_csv3.printSchema()
#
# print("#"*40)
# df_csv4 = (spark.read.format('csv').
#            option("header", True).
#            option("inferSchema", True).
#            load("/Users/harish/PycharmProjects/pythonProject/source_files/Contact_info.csv"))
#
# df_csv4.show()
# print(df_csv4.count())
# df_csv4.printSchema()

spark.read.format("com.databricks.spark.avro").load("/Users/harish/PycharmProjects/pythonProject/source_files/userdata1.avro").show()