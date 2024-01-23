# import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.connect.functions import concat_ws

spark = SparkSession.builder.master("local")\
    .appName("test") \
    .getOrCreate()

from pyspark.sql.functions import col,upper, lower, length, concat, initcap, explode,initcap, substring, instr
data = [("Rahul","Smith","USA","C"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL"),
    ("ramesh","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL"),
    ("rahul","Smith","USA","A"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL"),
    ("Jamessadhfsadhgasfghashgfashdgfghsadfa","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","K"),
    ("Maria","Jones","USA","FL")
  ]
columns = ["firstname","lastname","country","state_name"]
df = spark.createDataFrame(data = data, schema = columns)
df.show(n=5,truncate=25)

df.select(df.firstname, df.lastname).show(5)
df.select(col('firstname'), col('lastname')).show(2)
df.select(df['firstname'], df['last name'], df['country'], df['state']).show(2)
df.select(upper('firstname').alias('fn'), initcap('last name').alias('ln')).show(5)
df.select(df.colRegex("`^.*name*`")).show(2)
df.select("*").show(2)
df.select("*").filter(" firstname = 'Rahul' ").show()
df.select("*").filter("(firstname = 'Rahul' or lastname ='Rose') and state_name = 'NY' ").show()
df.select((concat(upper(df.firstname),lower(df['lastname']), df.state_name)).alias("FullName"), length(col("state_name")).alias("State_num_letters")).filter("length(state_name) >=2 ").display()
df.select((concat_ws(" ",upper(df.firstname),lower(df['lastname']), df.state_name)).alias("FullName"), length(col("state_name")).alias("State_num_letters")).filter("length(state_name) >=2 ").display()
print("df.columns",df.columns)
print("df.columns[0]",df.columns[0])

df1 = spark.read.format("json").option("multiline", "True").load("/Users/harish/PycharmProjects/pythonProject/source_files/Complex2.json")

df1.display()

df2 = df1.select("*", explode("people").alias("person_details")).drop("people")

df3 = df2.select(df2.person_details.age.alias("age"), df2.person_details.firstName.alias("fn"), df2.person_details.gender.alias("gender"), df2.person_details.lastName.alias("ln"), df2.person_details.number.alias("ph"))

df3.display()

from pyspark.sql.types import *
from pyspark.sql.functions import *


def flatten(df):
    # compute Complex Fields (Lists and Structs) in Schema
    complex_fields = dict([(field.name, field.dataType)
                           for field in df.schema.fields
                           if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
    while len(complex_fields) != 0:
        col_name = list(complex_fields.keys())[0]
        print("Processing :" + col_name + " Type : " + str(type(complex_fields[col_name])))

        # if StructType then convert all sub element to columns.
        # i.e. flatten structs
        if (type(complex_fields[col_name]) == StructType):
            expanded = [col(col_name + '.' + k).alias(col_name + '_' + k) for k in
                        [n.name for n in complex_fields[col_name]]]
            df = df.select("*", *expanded).drop(col_name)

        # if ArrayType then add the Array Elements as Rows using the explode function
        # i.e. explode Arrays
        elif (type(complex_fields[col_name]) == ArrayType):
            df = df.withColumn(col_name, explode_outer(col_name))

        # recompute remaining Complex Fields in Schema
        complex_fields = dict([(field.name, field.dataType)
                               for field in df.schema.fields
                               if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
    return df

json_file = spark.read.format("json").option("multiline", "True").load("dbfs:/FileStore/shared_uploads/kattubadinovember2023@gmail.com/SourceFiles/Complex2.json")

json_file.display()

json_flatten_df = flatten(json_file)

json_flatten_df.show()