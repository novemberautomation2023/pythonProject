from pyspark.sql import SparkSession
#from pyspark.sql.connect.functions import col
from pyspark.sql.functions import upper,col

spark = SparkSession.builder.master("local[1]").appName("test").getOrCreate()

#print(dir(spark))
# spark = SparkSession.builder \
#       .master("local[*]") \
#       .appName("test") \
#       .getOrCreate()

#print(help(spark.createDataFrame))
dataList = [("Java", 20000,4,5), ("Python", 100000,3,6), ("Scala", 3000,1,7),("PHP",2000,5,8)]
schema = ['Language','Salary','exp','age']
df1 =spark.createDataFrame(data=dataList, schema=schema)

dataList2 = [("Java",'1995'), ("Python",'1992'), ("Scala",'unknwn'),("PHP",'unknwn')]
schema2 = ['Language','year']
df2 = spark.createDataFrame(dataList2, schema=schema2)

df1.show()
df1.printSchema()
print(df1.rdd.getNumPartitions())
print(df1.count())
print(df1.columns)
print(df1.schema.json())
df1.createTempView('df1')
df2.createTempView("df2")
print("join after stmt")
df1.join(df2,['language'], how='inner'). \
withColumn('language', upper(col('language'))).show()
#df1.union(df2).show()
#df1.exceptAll(df2)

df2 = spark.sql('''select upper(a.language) as language, Salary, exp,year from df1 a, df2 b
          where a.language= b.language ''')

df2.show()






