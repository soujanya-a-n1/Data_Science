# 📊  Data Science Tasks

This repository contains completed tasks for the **CODTECH Internship**, focused on Data Cleaning (ETL) and Deep Learning (MNIST image classification) using Python.

---


## ✅ Task 1 – ETL Pipeline (Task1)

### 📌 Overview
Build an ETL (Extract, Transform, Load) pipeline to load data from a CSV, clean and preprocess it, and save the processed CSV for downstream analysis or modeling.

### 📂 Files
- `Task1/data.csv` — raw input data
- `Task1/etl_pipeline.py` — ETL script (reads `data.csv`, preprocesses, writes `processed_data.csv`)
- `Task1/processed_data.csv` — output (generated after running the script)

### 🛠 Dependencies
- pandas
- numpy
- scikit-learn

Install: `pip install pandas numpy scikit-learn`

### ▶️ Run
From the repository root:
```bash
python Task1/etl_pipeline.py
```
The script will read `Task1/data.csv` and write `Task1/processed_data.csv`.

---

## ✅ Task 2 – Deep Learning (MNIST)

### 📌 Overview
Train a simple neural network on the MNIST handwritten digits dataset using TensorFlow/Keras. The script trains the model, evaluates it, and saves accuracy/loss plots to `Task2/results/`.

### 📂 Files
- `Task2/model.py` — training script (creates `Task2/results/` automatically)
- `Task2/results/accuracy.png` — training vs. validation accuracy plot
- `Task2/results/loss.png` — training vs. validation loss plot

### 🛠 Dependencies
- tensorflow
- matplotlib
- numpy

Install: `pip install tensorflow matplotlib numpy`

### ▶️ Run
From the repository root:
```bash
python Task2/model.py
```
Note: training can take several minutes depending on your machine. The script creates the `Task2/results/` directory if it does not exist.

---

## 📝 Notes & Recommendations
- Use a virtual environment (venv or conda) to isolate dependencies.
- Consider adding `requirements.txt` files in each task directory for reproducibility.
- Optionally add `if __name__ == "__main__":` guards to scripts to avoid running on import.

---

If you'd like, I can also:
- Create `requirements.txt` files for each task ✅
- Add a short CI workflow to run fast smoke tests 🔧
- Add example outputs or short screenshots to the README 📸

---

#  Task 3 – End-to-End Data Science Project

## Project Title:
House Price Prediction Web Application

## Description:
This project demonstrates a complete end-to-end data science workflow including:
- Data collection
- Data preprocessing
- Feature engineering
- Machine learning model training
- Model deployment using Flask

A trained machine learning model predicts house prices based on user input features through a web interface.

## Objectives:
- Build a complete data science pipeline
- Train and evaluate a machine l

## Project Structure:
Task3/
│
├── data/
│ └── housing.csv
│
├── model/
│ └── model.pkl
│
├── templates/
│ └── index.html
│
├── train_model.py
├── app.py
├── requirements.txt


## Workflow:
1. Data Loading
2. Data Preprocessing
3. Feature Encoding
4. Train-Test Splitting
5. Model Training
6. Model Saving
7. Flask API Development
8. Web App Deployment

## Installation & Execution:

### Step 1: Clone Repository
git clone <your-github-repository-link>

### Step 2: Create Virtual Environment
python -m venv .venv


### Step 3: Activate Virtual Environment
.venv\Scripts\activate


### Step 4: Install Dependencies
pip install -r requirements.txt


### Step 5: Train Model
python train_model.py


### Step 6: Run Flask Application
python app.py


Open browser and visit:
http://127.0.0.1:5000

# Task 4  
## Optimization Model using Linear Programming and Python

This project is part of the ** Internship Program – Task 4**, where the objective is to solve a real-world **business optimization problem** using **Linear Programming techniques** and Python libraries such as **PuLP**.

---

## 📌 Problem Statement

A manufacturing company produces two products: **Product A** and **Product B**.  
Each product requires machine time and labor time. The company wants to determine the **optimal number of units to produce** in order to **maximize total profit**, subject to limited resources.

---

## 🎯 Objective

To **maximize profit** while efficiently utilizing:
- Machine hours
- Labor hours  

using **Linear Programming optimization techniques**.

---

## 🧮 Mathematical Model

Let:  
- x = units of Product A  
- y = units of Product B  

### Maximize:
40x + 30y


### Subject to constraints:
2x + y ≤ 40 (Machine hours)
x + 2y ≤ 60 (Labor hours)
x ≥ 0, y ≥ 0


---

## 🛠 Tools & Technologies Used

- Python  
- VS Code  
- Jupyter Notebook  
- PuLP (Linear Programming Library)  

---

## 📂 Project Files

TASK4_OPTIMIZATION
│
├── optimization.ipynb # Main notebook
└── requirements.txt # Required Python libraries


---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt

📊 Output
Status: Optimal
Product A units: 6.67
Product B units: 26.67
Maximum Profit = ₹1466.67
