# Building a Phishing Threat Data Catalog Using AWS and Apache Spark

## **Project Overview**

**Title:** **Building a Phishing Threat Data Catalog Using AWS and Apache Spark**

**Objective:** Develop an end-to-end system to collect, process, catalog, and analyze phishing threat data for uncovering patterns and providing actionable cybersecurity insights. This project includes data ingestion, cleaning, transformation, analysis, and visualization using AWS services and Apache Spark tools.

**Technologies Used:**

- **AWS Services:** S3, Lambda
- **Programming Languages:** Python, SQL
- **Big Data Technologies:** Apache Spark
- **Others:** Requests for API interaction, Matplotlib and Seaborn for data visualization

---

## **Project Architecture**

1. **Data Ingestion:**
   - Fetch phishing data from the PhishTank API using a Python script.
   - Store the ingested data in **AWS S3**.

2. **Data Processing:**
   - Use **Apache Spark** to process JSON data.
   - Clean the data and extract useful features (e.g., domain names).

3. **Data Storage:**
   - Store processed data in **Parquet format** in S3 for efficient querying.

4. **Data Analysis:**
   - Use SparkSQL to analyze the processed data.
   - Identify trends in phishing attacks, such as the most targeted domains.

5. **Data Visualization:**
   - Utilize **Jupyter Notebooks** or standalone Python scripts with **Matplotlib** and **Seaborn** for visual assessments of phishing threat data.

---

## **Step-by-Step Implementation Guide**

### **1. Setting Up AWS Resources**

- **Create an S3 Bucket:**
  - Use this bucket to store raw and processed phishing threat data.

- **Set Up IAM Roles:**
  - Configure roles with necessary permissions for accessing S3.

### **2. Data Ingestion**

- **Create a Python Script to Fetch Phishing Data:**

  ```python
  import boto3
  import requests
  import json
  from datetime import datetime

  def fetch_phishing_data():
      phish_url = 'https://data.phishtank.com/data/online-valid.json'
      response = requests.get(phish_url)
      return response.json()

  s3 = boto3.client('s3')
  bucket = 'your-bucket'
  timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
  filename = f'phishtank_{timestamp}.json'
  s3.put_object(Bucket=bucket, Key=f'phishing_threat_data/raw/{filename}', Body=json.dumps(fetch_phishing_data()))
  ```

- **Run the Script:**
  - The script should be set up to run at regular intervals for continuous data ingestion.

### **3. Data Processing with Apache Spark**

- **Set Up Spark for Data Processing:**
  - Initialize a Spark session and read data from S3:
  
  ```python
  from pyspark.sql import SparkSession

  spark = SparkSession.builder.appName('PhishingThreatDataCatalog').getOrCreate()
  phishing_df = spark.read.json('s3://your-bucket/phishing_threat_data/raw/*.json')
  ```

- **Data Cleaning and Transformation:**

  ```python
  phishing_df = phishing_df.dropna(how='any')
  # Extract domain from URL (additional processing)
  ```

### **4. Data Analysis with SparkSQL**

- **Perform Analysis:**
  - Analyze top domains targeted by phishing attacks:

  ```python
  phishing_df.createOrReplaceTempView('phishing_data')
  result = spark.sql('SELECT domain, COUNT(*) as attack_count FROM phishing_data GROUP BY domain ORDER BY attack_count DESC LIMIT 10')
  ```

### **5. Data Visualization**

- **Visualize Results Using Matplotlib and Seaborn:**

  ```python
  import pandas as pd
  import matplotlib.pyplot as plt
  import seaborn as sns

  result.toPandas().to_csv('top_domains.csv')  # Example to save results to CSV
  data = pd.read_csv('top_domains.csv')

  plt.figure(figsize=(12, 6))
  sns.barplot(data=data, x='domain', y='attack_count', palette='magma')
  plt.title('Top 10 Most Targeted Domains by Phishing Attacks')
  plt.xlabel('Domain')
  plt.ylabel('Number of Attacks')
  plt.xticks(rotation=45)
  plt.show()
  ```

---

## **Project Documentation**

- **README.md:**

  - **Project Title:** Building a Phishing Threat Data Catalog Using AWS and Apache Spark

  - **Description:** An end-to-end data engineering project that collects, processes, catalogs, and analyzes phishing threat data to uncover patterns and provide actionable cybersecurity insights.

  - **Contents:**
    - **Introduction**
    - **Project Architecture**
    - **Technologies Used**
    - **Dataset Information**
    - **Setup Instructions**
      - Prerequisites
      - AWS Configuration
    - **Running the Project**
    - **Data Processing Steps**
    - **Data Analysis and Results**
    - **Visualization**
    - **Conclusion**

  - **License and Contribution Guidelines**

- **Code Organization:**

  ```
  ├── README.md
  ├── data
  │   └── sample_data.json
  ├── notebooks
  │   └── visualization.ipynb
  └── scripts
      ├── data_analysis.py
      ├── data_ingestion.py
      ├── data_processing.py
      ├── modeling.py
      └── visualization.py
  ```

- **Comments and Docstrings:**
  - Include detailed docstrings for all functions and classes.
  - Comment on complex code blocks to explain the logic.

---

## **Best Practices**

- **Use Version Control:**
  - Initialize a Git repository and commit changes regularly.

    ```
    git init
    git add .
    git commit -m "Initial commit with project structure and documentation"
    ```

- **Handle Exceptions:**
  - Add error handling in Python scripts and logging to capture and debug issues.

- **Security:**
  - **Do not expose AWS credentials** in your code.
  - Use IAM roles for permissions.

- **Optimization:**
  - Optimize data processing with Spark configurations.
  - Monitor performance and scale as necessary.

- **Cleanup Resources:**
  - Terminate unnecessary resources and remove unused data in S3.

---

## **Demonstrating Skills**

- **PySpark and SQL:**
  - Competently leverage Spark for data processing and analysis.

- **Data Engineering Concepts:**
  - Implement efficient data ingestion and processing pipelines.

- **Data Analysis and Visualization:**
  - Reflect on patterns from data through visualization tools.

---

## **Additional Enhancements**

- **Implement Unit Tests:**
  - Use `pytest` for testing data ingestion and processing functions.

- **Continuous Integration:**
  - Set up GitHub Actions for automated testing.

- **Machine Learning Integration:**
  - Expand on the modeling.py script for predictive analytics.

- **Data Quality Checks:**
  - Incorporate data validation and quality checks into the ETL process.
