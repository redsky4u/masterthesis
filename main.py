# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'your_dataset.csv'  #TODO: change file name
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Display basic information about the dataset
print("\nDataset Information:")
print(df.info())

# Display summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Visualize missing values using a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()

# Plot histograms for numerical columns
df.hist(bins=30, figsize=(15, 10), color='blue', edgecolor='black')
plt.suptitle('Histograms of Numerical Columns')
plt.show()

# Box plots for numerical columns to check for outliers
plt.figure(figsize=(15, 8))
sns.boxplot(data=df.select_dtypes(include=[np.number]), orient='h')
plt.title('Box Plots of Numerical Columns')
plt.show()

# Count plots for categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    plt.figure(figsize=(10, 5))
    sns.countplot(y=col, data=df)
    plt.title(f'Count Plot of {col}')
    plt.show()

# Correlation matrix and heatmap for numerical columns
correlation_matrix = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()

# Pairplot for numerical columns to visualize relationships
sns.pairplot(df.select_dtypes(include=[np.number]))
plt.suptitle('Pairplot of Numerical Columns', y=1.02)
plt.show()

#---

# Read the CSV file
file_path = 'your_file.csv'  #TODO: change file
df = pd.read_csv(file_path)

# Display basic information about the dataset
print("Dataset Information:")
print(df.info())

# Display the first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(df.head())

# Assuming 'Company' is in column A and 'Year' is in column B
company_column = df.columns[0]  # First column (A)
year_column = df.columns[1]     # Second column (B)

# Create a bar plot
plt.figure(figsize=(12, 6))
plt.bar(df[company_column], df[year_column])

# Customize the plot
plt.title('Companies by Year')
plt.xlabel('Company Names')
plt.ylabel('Year')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Show the plot
plt.show()
