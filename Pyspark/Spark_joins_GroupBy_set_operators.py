# Databricks notebook source
import pyspark
from pyspark.sql import SparkSession

emp = [(1, "Smith", -1, "2018", "10", "M", 3000), \
       (2, "Rose", 1, "2010", "20", "M", 4000), \
       (3, "Williams", 1, "2010", "30", "M", 1000), \
       (4, "Jones", 10, "2005", "10", "F", 2000), \
       (5, "Brown", 2, "2010", "40", "", 1000), \
       (6, "Brown", 2, "2010", "50", "", 500) \
       ]
empColumns = ["eno", "ename", "mgr_id", "year_joined", \
              "dept_id", "gender", "salary"]

emp = spark.createDataFrame(data=emp, schema=empColumns)
emp.printSchema()
emp.show(truncate=False)

dept = [("Finance", 10), \
        ("Marketing", 20), \
        ("Sales", 30), \
        ("IT", 40),
        ("HR", 60) \
        ]
deptColumns = ["dept_name", "dept_id"]
dept = spark.createDataFrame(data=dept, schema=deptColumns)
dept.printSchema()
dept.show(truncate=False)

# COMMAND ----------

join_df = emp.join(dept, emp.dept_id == dept.dept_id, 'inner')

join_df.show()

# COMMAND ----------

emp.join(dept, 'dept_id', 'inner').show()

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, 'left').show()

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, 'right').show()

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, 'full').show()

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, 'left').show()

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, 'leftsemi').show()  # inner join without rightside df columns

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, 'leftanti').show()  # s minus t on key_column

# COMMAND ----------

emp.join(dept, [emp.dept_id == dept.dept_id, emp.mgr_id == dept.dept_id], 'inner').show()

# COMMAND ----------

emp.join(dept, ['dept'], 'inner').join(df3, ['dept'],
                                       'left')  # Never do spark join with Big data set and small dataset( profile, ref postal)

# COMMAND ----------


from pyspark.sql.functions import col

emp.alias("emp1").join(emp.alias("emp2"), \
                       col("emp1.mgr_id") == col("emp2.eno"), "inner") \
    .select(col("emp1.eno"), col("emp1.ename"), \
            col("emp2.eno").alias("mgr_id"), \
            col("emp2.ename").alias("ename")) \
    .show(truncate=False)

# COMMAND ----------

from pyspark.sql.functions import sum, avg, min, col, max, count, upper, lower, regexp_replace, round

simpleData = [("James", "Sales", "NY", 90000, 34, 10000),
              ("Michael", "Sales", "NY", 86000, 56, 20000),
              ("Robert", "Sales", "CA", 81000, 30, 23000),
              ("Maria", "Finance", "CA", 90000, 24, 23000),
              ("Raman", "Finance", "CA", 99000, 40, 24000),
              ("Scott", "Finance", "NY", 83000, 36, 19000),
              ("Jen", "Finance", "NY", 79000, 53, 15000),
              ("Jeff", "Marketing", "CA", 80000, 25, 18000),
              ("", "Marketing", "NY", 91000, 50, 21000)
              ]

schema = ["employee_name", "department", "state", "salary", "age", "bonus"]
df = spark.createDataFrame(data=simpleData, schema=schema)
df.printSchema()
df.show(truncate=False)

# COMMAND ----------

# summary = df.select(df.salary, df['age'], 'bonus').summary()#.where("summary in ('count', 'mean') ")

summary2 = df.summary()
summary2.display()
print(type(summary2))
# summary = df.summary().select('summary','salary','bonus').where("summary in ('count', 'mean','min','max') ")

# display(summary)

summary2.select('summary', 'state', 'salary', 'bonus').filter("summary in ('count','mean','min') ").display()

# COMMAND ----------

df.select(sum(col('salary')).alias("sum_sal"), count("*").alias("num_of_records"), \
          avg(df.bonus).alias("average_sal"), min('salary').alias("min_sal"), max(df.salary).alias("max_sal")).display()

# COMMAND ----------

# df.groupBy('department').count().display()
df.groupBy('department').sum().show()
df.groupBy('department').min().show()
df.groupBy('department').max().show()

# COMMAND ----------

df.groupBy("department", "state").sum('bonus').show()

# COMMAND ----------


from pyspark.sql.functions import ceil, floor

df.groupBy("department") \
    .agg(sum("salary").alias("sum_salary"),
         avg("salary").alias("avg_salary"), \
         ceil(avg("salary").alias("avg_salary")), \
         sum("bonus").alias("sum_bonus"), \
         max("bonus").alias("max_bonus"), \
         min("salary"), \
         count('department')
         ) \
    .show(truncate=False)

# COMMAND ----------

import pyspark
from pyspark.sql import SparkSession

simpleData = [(1, "James", "Sales", "NY", 90000), \
              (2, "Michael", "Sales", "NY", 86000), \
              (3, "Robert", "Sales", "CA", 81000), \
              (4, "Maria", "Finance", "CA", 90000), \
              (1, "James", "Sales", "NY", 90000)
              ]

columns = ["emp_id", "employee_name", "department", "state", "salary"]
df = spark.createDataFrame(data=simpleData, schema=columns)
df.printSchema()
df.show(truncate=False)

# COMMAND ----------

# DBTITLE 0,Pyspark DataFrame creation
# MAGIC %md #Set Operators

# COMMAND ----------

import pyspark
from pyspark.sql import SparkSession

simpleData2 = [(1, "James", "Sales", "NY", 90000), \
               (2, "Michael", "Sales", "NY", 86000), \
               (5, "Sonja", "Sales", "OH", 45000), \
               (6, "Randy H", "Finance", "NJ", 40000)
               ]

columns = ["emp_id", "employee_name", "department", "state", "salary"]
df2 = spark.createDataFrame(data=simpleData2, schema=columns)
df2.printSchema()
df2.show(truncate=False)

# COMMAND ----------

# MAGIC %md ##union

# COMMAND ----------

unionDF = df.union(df2)
unionDF.show(truncate=False)

# COMMAND ----------

# MAGIC %md ##unionall

# COMMAND ----------

unionAllDF = df.unionAll(df2)
unionAllDF.show(truncate=False)

# COMMAND ----------

# MAGIC %md ##creationg sql union in pyspark

# COMMAND ----------

disDF = df.unionAll(df2).distinct()
disDF.show()

disDF1 = df.union(df2).distinct()
disDF1.show()

# COMMAND ----------

# MAGIC %md ##Intersect

# COMMAND ----------

df.show()
import pyspark
from pyspark.sql import SparkSession

simpleData2 = [(1, "James", "Sales", "NY", 90000), \
               (2, "Michael", "Sales", "NY", 86000), \
               (5, "Sonja", "Sales", "OH", 45000), \
               (6, "Randy H", "Finance", "NJ", 40000),
               (1, "James", "Sales", "NY", 90000)
               ]

columns = ["emp_id", "employee_name", "department", "state", "salary"]
df2 = spark.createDataFrame(data=simpleData2, schema=columns)
df2.printSchema()
df2.show(truncate=False)

# COMMAND ----------

df.intersect(df2).show()
df.intersectAll(df2).show()

# COMMAND ----------

# MAGIC %md ##Except

# COMMAND ----------

df.show()
import pyspark
from pyspark.sql import SparkSession

simpleData2 = [(1, "James", "Sales", "NY", 90000), \
               (2, "Michael", "Sales", "NY", 86000), \
               (5, "Sonja", "Sales", "OH", 45000), \
               (6, "Randy H", "Finance", "NJ", 40000)
               ]

columns = ["emp_id", "employee_name", "department", "state", "salary"]
df2 = spark.createDataFrame(data=simpleData2, schema=columns)
df2.printSchema()
df2.show(truncate=False)

# COMMAND ----------

df.exceptAll(df2).distinct().show()
df2.exceptAll(df).show()

df.distinct().exceptAll(df2).show()  # we will use to identify missing  records it accounts duplicate data also

# COMMAND ----------

import pyspark
from pyspark.sql import SparkSession

emp = [(1, "Smith", -1, "2018", "10", "M", 3000), \
       (2, "Rose", 1, "2010", "20", "M", 4000), \
       (3, "Williams", 1, "2010", "30", "M", 1000), \
       (4, "Jones", 10, "2005", "10", "F", 2000), \
       (5, "Brown", 2, "2010", "40", "", 1000), \
       (6, "Brown", 2, "2010", "50", "", 500) \
       ]
empColumns = ["eno", "ename", "mgr_id", "year_joined", \
              "dept_id", "gender", "salary"]

emp = spark.createDataFrame(data=emp, schema=empColumns)
emp.printSchema()
emp.show(truncate=False)

dept = [("Finance", 10), \
        ("Marketing", 20), \
        ("Sales", 30), \
        ("IT", 40),
        ("HR", 60) \
        ]
deptColumns = ["dept_name", "dept_id"]
dept = spark.createDataFrame(data=dept, schema=deptColumns)
dept.printSchema()
dept.show(truncate=False)

# COMMAND ----------

emp.unionByName(allowMissingColumns=True, other=dept).display()

# COMMAND ----------

df1 = spark.createDataFrame(
    [("a", 1), ("a", 1), ("a", 1), ("a", 2), ("b", 3), ("c", 4)], ["C1", "C2"])
df2 = spark.createDataFrame([("a", 1), ("b", 3)], ["C1", "C2"])
df1.show()
df2.show()
# df1.distinct().exceptAll(df2).show()
df1.exceptAll(df2).show()

# COMMAND ----------

df1 = spark.createDataFrame(
    [("a", 1), ("a", 1), ("a", 1), ("a", 2), ("b", 3), ("c", 4)], ["C1", "C2"])
df2 = spark.createDataFrame([("a", 1), ("b", 3), ("a", 1)], ["C1", "C2"])
df1.show()
df2.show()

df1.intersect(df2).show()
df1.intersectAll(df2).show()

df1.exceptAll(df2).show()

# COMMAND ----------

df1.intersectAll(df2).show()

# COMMAND ----------

# MAGIC %md # Sorting data

# COMMAND ----------

import pyspark
from pyspark.sql import SparkSession

emp = [(1, "Smith", -1, "2018", "10", "M", 3000), \
       (2, "Rose", 1, "2010", "20", "M", 4000), \
       (3, "Williams", 1, "2010", "30", "M", 1000), \
       (4, "Jones", 10, "2005", "10", "F", 2000), \
       (5, "Brown", 2, "2010", "40", "", 1000), \
       (6, "Brown", 2, "2010", "50", "", 500) \
       ]
empColumns = ["eno", "ename", "mgr_id", "year_joined", \
              "dept_id", "gender", "salary"]

emp = spark.createDataFrame(data=emp, schema=empColumns)
emp.printSchema()
emp.show(truncate=False)

dept = [("Finance", 10), \
        ("Marketing", 20), \
        ("Sales", 30), \
        ("IT", 40),
        ("HR", 60) \
        ]
deptColumns = ["dept_name", "dept_id"]
dept = spark.createDataFrame(data=dept, schema=deptColumns)
dept.printSchema()
dept.show(truncate=False)

# COMMAND ----------

emp.sort(emp.eno.desc(), emp.salary.asc()).show()
emp.orderBy(emp.eno.asc()).show()

# COMMAND ----------

emp.select('eno', 'ename', 'gender').sort(emp.eno.asc()).show()
emp.select('eno', 'ename', 'gender').orderBy(emp.eno.asc(), emp.ename.desc()).show()

# COMMAND ----------

emp.show()

# COMMAND ----------

# MAGIC %md #Fill Null values

# COMMAND ----------


data = [
    (1, "James", None, "M"),
    (2, "Anna", "NY", ""),
    (None, "Julia", None, None)
]

columns = ["id", "name", "state", "gender"]
df = spark.createDataFrame(data, columns)
df.show()

# COMMAND ----------

df.fillna('unknwn').show()

df.fillna(0).show()

# COMMAND ----------

df.withColumn('gender', when(df.gender == "", None).otherwise(df.gender)).fillna("unknwn").fillna(0).show()

# COMMAND ----------

from pyspark.sql.functions import when

df.na.fill({"state": "unknownst", "gender": "unkgen"}).show()

# COMMAND ----------

df2 = df.select("*", when(df.gender == "M", "Male")
                .when(df.gender == "F", "Female")
                .when(df.gender.isNull(), "")
                .otherwise(df.gender).alias("new_gender"))
df2.show()

# COMMAND ----------

data = [
    (1, "James", None, "M"),
    (1, "James", None, "M"),
    (2, "Anna", "NY", ""),
    (None, "Julia", None, None),
    (1, "George", None, "M")
]

columns = ["id", "name", "state", "gender"]
df = spark.createDataFrame(data, columns)
df.show()

df.distinct().show()

# COMMAND ----------

df.dropDuplicates().show()

# COMMAND ----------

df.dropDuplicates(['id']).show()

# COMMAND ----------

df.collect()

# COMMAND ----------

df.sample(0.1, seed=1).show()

# COMMAND ----------

df.sample(0.1, seed=3).show()

# COMMAND ----------

# MAGIC %md #PartitionBy

# COMMAND ----------

simpleData = (("James", "Sales", 3000), \
              ("Michael", "Sales", 4600), \
              ("Robert", "Sales", 4100), \
              ("Maria", "Finance", 3000), \
              ("James", "Sales", 3000), \
              ("Scott", "Finance", 3300), \
              ("Jen", "Finance", 3900), \
              ("Jeff", "Marketing", 3000), \
              ("Kumar", "Marketing", 2000), \
              ("Saif", "Sales", 4100) \
              )

columns = ["employee_name", "department", "salary"]
df = spark.createDataFrame(data=simpleData, schema=columns)
df.printSchema()
df.show(truncate=False)

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, rank, dense_rank, partitionBy

windowSpec = Window.partitionBy("department").orderBy("salary")

df.withColumn("row_number", row_number().over(windowSpec)) \
    .show(truncate=False)

# COMMAND ----------

df.withColumn("rank", rank().over(windowSpec)).show()
df.withColumn('dense_rank', dense_rank().over(windowSpec)).show()

# COMMAND ----------

windowSpecAgg = Window.partitionBy("department")
from pyspark.sql.functions import col, avg, sum, min, max, row_number

df.withColumn("row", row_number().over(windowSpec)) \
    .withColumn("avg", avg(col("salary")).over(windowSpecAgg)) \
    .withColumn("sum", sum(col("salary")).over(windowSpecAgg)) \
    .withColumn("min", min(col("salary")).over(windowSpecAgg)) \
    .withColumn("max", max(col("salary")).over(windowSpecAgg)) \
    .where(col("row") == 1).select("department", "avg", "sum", "min", "max") \
    .show()

# COMMAND ----------

from pyspark.sql.functions import cume_dist

df.withColumn("cume_dist", cume_dist().over(windowSpec)) \
    .show()

# COMMAND ----------


# COMMAND ----------

from pyspark.sql import Row

row = Row(name="James", age=40)
print(row[0] + "," + str(row[1]))

# COMMAND ----------

Row2 = Row(name='James', age=21)
Row3 = Row(name="hari", age=23)

# COMMAND ----------

Row2.name

# COMMAND ----------

spark.createDataFrame([row, Row2, Row3]).show()

# COMMAND ----------

# MAGIC %md #datefunctions

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

data = [["1", "2020-02-01"], ["2", "2019-03-01"], ["3", "2021-03-01"]]
df = spark.createDataFrame(data, ["id", "input"])
df.show()
df.printSchema()

# COMMAND ----------

df.select(current_date().alias("current_date")
          ).show(1)

# COMMAND ----------

df.select(col("input"),
          date_format(col("input"), "MM-dd-yyyy").alias("date_format")
          ).show()

# COMMAND ----------

df.select(col("input"),
          to_date(col("input"), "yyy-MM-dd").alias("to_date")
          ).printSchema()

# COMMAND ----------

df.select(col("input"),
          datediff(current_date(), col("input")).alias("datediff")
          ).show()

# COMMAND ----------

df.select(col("input"),
          months_between(current_date(), col("input")).alias("months_between")
          ).show()

# COMMAND ----------

df.select(col("input"),
          add_months(col("input"), 3).alias("add_months"),
          add_months(col("input"), -3).alias("sub_months"),
          date_add(col("input"), 4).alias("date_add"),
          date_sub(col("input"), 4).alias("date_sub")
          ).show()

# COMMAND ----------

df.select(col("input"),
          year(col("input")).alias("year"),
          month(col("input")).alias("month"),
          next_day(col("input"), "Sunday").alias("next_day"),
          weekofyear(col("input")).alias("weekofyear"),
          quarter(col("input")).alias("quarter")
          ).show()

# COMMAND ----------

df.select(col("input"),
          dayofweek(col("input")).alias("dayofweek"),
          dayofmonth(col("input")).alias("dayofmonth"),
          dayofyear(col("input")).alias("dayofyear"),
          ).show()

# COMMAND ----------

data = [["1", "2020-02-01 11:01:19.06"], ["2", "2019-03-01 12:01:19.406"], ["3", "2021-03-01 12:01:19.406"]]
df3 = spark.createDataFrame(data, ["id", "input"])
df3.show(truncate=False)

# COMMAND ----------

df3.select(col("input"),
           hour(col("input")).alias("hour"),
           minute(col("input")).alias("minute"),
           second(col("input")).alias("second")
           ).show(truncate=False)

# COMMAND ----------


