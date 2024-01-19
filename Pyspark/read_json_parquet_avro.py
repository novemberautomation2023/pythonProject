from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]").appName("csv").getOrCreate()
spark.read.format('json').load("dbfs:/FileStore/shared_uploads/kattubadinovember2023@gmail.com/SourceFiles/singleline_2.json").show()

spark.read.format('json').option("multiline", True).load('dbfs:/FileStore/shared_uploads/kattubadinovember2023@gmail.com/SourceFiles/sample1.json').show()

spark.read.parquet("dbfs:/FileStore/shared_uploads/kattubadinovember2023@gmail.com/SourceFiles/userdata1.parquet").show()

spark.read.format("avro").load("dbfs:/FileStore/shared_uploads/kattubadinovember2023@gmail.com/SourceFiles/userdata1.avro").show()