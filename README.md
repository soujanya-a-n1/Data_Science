# 📊 CODTECH Internship – Data Science Tasks

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
