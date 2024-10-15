# Data Analysis Script Using PySpark for Phishing Threat Data
from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName('PhishingThreatDataCatalog').getOrCreate()

# Load Processed Data
phishing_df = spark.read.parquet('s3://your-bucket/phishing_threat_data/processed/')

# Perform Analysis
phishing_df.createOrReplaceTempView('phishing_data')

# Top 10 Most Targeted Domains

# Run SQL Query
result = spark.sql('SELECT domain, COUNT(*) as attack_count FROM phishing_data GROUP BY domain ORDER BY attack_count DESC LIMIT 10')
result.show()

# Save Output
result.write.csv('s3://your-bucket/phishing_threat_data/output/top_domains.csv', mode='overwrite')
