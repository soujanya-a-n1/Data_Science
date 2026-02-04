# Task 1: Data Cleaning & Preprocessing (ETL Pipeline)

## 📌 Task Overview
This task focuses on building a basic **ETL (Extract, Transform, Load) pipeline** using Python.  
The goal is to extract data from a CSV file, clean and preprocess the data, and save the processed data into a new CSV file for further analysis or machine learning.

---

## 🛠 Tools & Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- VS Code  

---

## 📂 Project Structure

Task1_Data_Preprocessing/
│
├── data.csv # Raw input dataset
├── etl_pipeline.py # Python ETL script
├── processed_data.csv # Output processed dataset
└── README.md # Task documentation


---

## 🔄 ETL Pipeline Steps

### 1️⃣ Extract
- Load data from a CSV file using Pandas.

### 2️⃣ Transform
- Handle missing values using mean imputation.
- Encode categorical variables into numerical values.
- Scale numerical features for consistency.

### 3️⃣ Load
- Save the cleaned and transformed data into a new CSV file.

---

## ▶️ How to Run the Code

### Step 1: Install Python
Download and install Python from:  
https://www.python.org/

Make sure Python is added to PATH.

---

### Step 2: Install Required Libraries
Open Terminal / VS Code terminal and run:

```bash
pip install pandas numpy scikit-learn


### step 3: run_etl_pipeline:
  description: Run the ETL pipeline script
  commands:
    - cd Task1_Data_Preprocessing
    - python etl_pipeline.py
