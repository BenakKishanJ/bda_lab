from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
from pyspark.sql.functions import col, count

sc = SparkContext()
spark = SQLContext(sc)
input_file = "file:///home/cloudera/posts.txt"
rdd = sc.textFile(input_file)

cleaned_rdd = rdd.map(lambda line: ''.join(
    ch.lower() if ch.isalnum() or ch.isspace() else ' ' for ch in line))

words_rdd = cleaned_rdd.flatMap(lambda line: line.split())

stopwords = set(["the", "is", "and", "to", "of", "in", "a", "for", "on",
                "with", "this", "that", "it", "as", "at", "be", "by", "an", "are", "i"])

filtered_rdd = words_rdd.filter(lambda w: w not in stopwords and w != "")

row_rdd = filtered_rdd.map(lambda w: Row(word=w))

df = spark.createDataFrame(row_rdd)
df = df.groupBy("word").count()
df = df.sort(df["count"].desc())

top_n = 10
results = df.take(top_n)

print("Word \t Count")
for r, c in results:
    print("%s\t%d" % (r, c))

# sc.stop()
