# Data Visualization Script Using Matplotlib and Seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data for Visualization
result = pd.read_csv('s3://your-bucket/phishing_threat_data/output/top_domains.csv')

# Plotting
plt.figure(figsize=(12, 6))
sns.barplot(data=result, x='domain', y='attack_count', palette='magma')
plt.title('Top 10 Most Targeted Domains by Phishing Attacks')
plt.xlabel('Domain')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=45)
plt.show()
