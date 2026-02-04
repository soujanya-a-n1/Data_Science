# ETL PIPELINE FOR CODETECH INTERNSHIP

# 1. Import libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

# 2. EXTRACT: Read data
data = pd.read_csv("data.csv")
print("Original Data:")
print(data)

# 3. TRANSFORM: Handle missing values
# Use assignment instead of inplace to avoid FutureWarning about chained assignment
data['Age'] = data['Age'].fillna(data['Age'].mean())
data['Salary'] = data['Salary'].fillna(data['Salary'].mean())

# 4. Encode categorical columns
# Use separate encoders to avoid accidental reuse across columns
le_gender = LabelEncoder()
le_dept = LabelEncoder()
data['Gender'] = le_gender.fit_transform(data['Gender'])
data['Department'] = le_dept.fit_transform(data['Department'])

# 5. Scale numerical columns
scaler = StandardScaler()
data[['Age', 'Salary']] = scaler.fit_transform(data[['Age', 'Salary']])

print("\nTransformed Data:")
print(data)

# 6. LOAD: Save final processed data
data.to_csv("processed_data.csv", index=False)

print("\nETL Pipeline completed successfully!")
