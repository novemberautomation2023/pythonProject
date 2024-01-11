from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder \
      .master("local[*]") \
      .appName("test") \
      .getOrCreate()

data1 = [(1,'Sreeni'),(2,'Raghav'),(3,"hari")]
#schema2 = ['id','name'] # Check on how to pass datatype
schema2 = 'id integer, name string'
df = spark.createDataFrame(data=data1,schema=schema2)
#Source = spark.createDataFrame([(111,'Sreeni'),(222,'ABC')],['Sno','TestName'])

df.show()

df.printSchema()

print(dir(spark))

print("before", id(df))

df = df.withColumn("test",lit('test'))

print("after",id(df))

data2 = [{'id':1, 'name':'Raghav'}, {'id':2, 'name':'Ram'}]

schema = ['id','name']

df2 = spark.createDataFrame(data=data2,schema=schema)

df2.show()

df2.createTempView("so")

spark.sql("select * from so").show()

data = [(1,"sreeni", 20), (2, "ram", 21), (3, "raghav", 22)]

schema = StructType([
    StructField("id",IntegerType(),True),
    StructField("name",StringType(),True),
    StructField("age",IntegerType(), True)]
)

df3 = spark.createDataFrame(data=data,schema=schema)

df3.show()
print(df3.rdd.getNumPartitions())
print(df.count())
print(df3.describe('name'))
print(df.columns)
print(df.schema.json())



#http://localhost:4040
