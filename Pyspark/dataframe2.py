"""
This file is created to work on spark dataframe
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import upper, col,lower, lpad,length,substring,instr
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType

spark = (SparkSession.builder.\
         appName("dataframe").getOrCreate())

dataList = [("Javahsfgdjshafghdsgfhasdgfhsadghsad", "2000357452364532674567325426732546230"), ("Python", "10000")]
#schema = 'language string, fee string'
schema = ['language' , 'fee']
df1 = spark.createDataFrame(data=dataList, schema=schema)
#df1.show(n=2,truncate=8,vertical=True)
df1.show()
df1.printSchema()
print('#'*40)
data = [(1,'Sreeni',23), (2, 'Raghav',24)]

schema = StructType([StructField("id",IntegerType(),nullable=False),
                     StructField("name", StringType(), nullable=True),
                     StructField('age',IntegerType(),nullable=False)
                     ])

df2 = spark.createDataFrame(data=data, schema=schema)
df2.show()
df2.printSchema()
print(id(df2))

print("after updating")
df2 = df2.withColumn('name', upper(col('name')))

print("after updating2")
df2.show()
print(id(df2))


