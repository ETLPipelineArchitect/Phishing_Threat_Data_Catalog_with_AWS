# Data Ingestion Script for Phishing Threat Data
import boto3
import requests
import json
from datetime import datetime

# Function to fetch phishing data from PhishTank
def fetch_phishing_data():
    phish_url = 'https://data.phishtank.com/data/online-valid.json'
    response = requests.get(phish_url)
    return response.json()

# Upload data to S3
s3 = boto3.client('s3')
bucket = 'your-bucket'
timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
filename = f'phishtank_{timestamp}.json'
s3.put_object(Bucket=bucket, Key=f'phishing_threat_data/raw/{filename}', Body=json.dumps(fetch_phishing_data()))
