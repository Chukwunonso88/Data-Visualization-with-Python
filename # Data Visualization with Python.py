#   Data Visualization with Python 
import pandas as pd

# Load dataset
df = pd.read_csv("/mnt/data/Africa_climate_change.csv")

# Display first 5 rows
print(df.head())

# Basic info
print(df.info())

# Summary statistics
print(df.describe())

#Cleaning Data

# Check for missing values
print(df.isnull().sum())

# Drop or fill missing values if necessary
df = df.dropna()  # or df.fillna(method='ffill')

# Ensure correct data types
df['Year'] = df['Year'].astype(int)

# to eliminate irrelevant columns (like “Unnamed” index columns), drop them:
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

#Plot Average Temperature Fluctuations
import matplotlib.pyplot as plt
import seaborn as sns

# Filter for Tunisia and Cameroon
subset = df[df['Country'].isin(['Tunisia', 'Cameroon'])]

plt.figure(figsize=(10,6))
sns.lineplot(data=subset, x='Year', y='AvgTemp', hue='Country')
plt.title("Average Temperature Fluctuations (Tunisia vs Cameroon)")
plt.xlabel("Year")
plt.ylabel("Average Temperature (°C)")
plt.grid(True)
plt.show()

#Zoom in on 1980–2005
subset_zoom = subset[(subset['Year'] >= 1980) & (subset['Year'] <= 2005)]

plt.figure(figsize=(10,6))
sns.lineplot(data=subset_zoom, x='Year', y='AvgTemp', hue='Country')
plt.title("Average Temperature Fluctuations (1980–2005)")
plt.xlabel("Year")
plt.ylabel("Average Temperature (°C)")
plt.show()


#Average Temperature per Country
avg_temp = df.groupby('Country')['AvgTemp'].mean().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(data=avg_temp, x='Country', y='AvgTemp', palette='viridis')
plt.title("Average Temperature per Country (1980–2023)")
plt.ylabel("Average Temperature (°C)")
plt.show()