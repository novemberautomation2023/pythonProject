# import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.connect.functions import concat_ws

spark = SparkSession.builder.master("local")\
    .appName("test") \
    .getOrCreate()

from pyspark.sql.functions import col,upper, lit,lower, length, concat, initcap, explode,initcap, substring, instr


spark.sql("select count(*), eno from emp group by eno having count(*)>1").show()
spark.sql("select * from emp inner join dept on emp.dept_id=dept.dept_id").show()
spark.sql("select * from global_temp.emp_global").show(1)
spark.sql("select * from emp where dept_id=10").show(1)

dept = [("Finance",10), \
    ("Marketing",20), \
    ("Sales",30), \
    ("IT",40) \
  ]
deptColumns = ["dept_name","dept_id"]
dept = spark.createDataFrame(data=dept, schema = deptColumns)
dept.printSchema()
dept.show(truncate=False)

dept.withColumn("dept_country", lit('IND')).show()
dept.withColumn("dept_short_name", substring(col('dept_name'),1,2)).show()
dept.withColumn("dept_name", upper(substring(col('dept_name'),1,2))).withColumn('dept_id2',col('dept_id')*100).show()
dept.withColumn("dept_id", col('dept_id').cast('integer')).printSchema()
dept.withColumn("dept_id", col('dept_id').cast('integer')).withColumnRenamed("dept_id","dept_no").printSchema()