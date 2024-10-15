# Data Processing Script Using PySpark for Phishing Threat Data
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, regexp_replace, udf
from pyspark.sql.types import StringType
import re

# Initialize Spark Session
spark = SparkSession.builder.appName('PhishingThreatDataCatalog').getOrCreate()

# Read Data from S3
phishing_df = spark.read.json('s3://your-bucket/phishing_threat_data/raw/*.json')

# Data Cleaning and Transformation
phishing_df = phishing_df.dropna(how='any')
phishing_df = phishing_df.withColumn('submission_time', to_timestamp(col('submission_time'),'yyyy-MM-dd HH:mm:ss'))

# Extract Domain from URL

# Define how to extract domain

def extract_domain(url):
    pattern = r'https?://([^/]+)/?'
    match = re.match(pattern, url)
    return match.group(1) if match else None

extract_domain_udf = udf(extract_domain, StringType())
phishing_df = phishing_df.withColumn('domain', extract_domain_udf(col('url')))
phishing_df = phishing_df.filter(col('domain').isNotNull())

# Save Processed Data to S3 in Parquet Format
phishing_df.write.parquet('s3://your-bucket/phishing_threat_data/processed/', mode='overwrite')
