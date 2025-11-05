# 📊 DataForge: Automated EDA & Analytics Platform

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> *"Data speaks, but only if you know how to listen. DataForge translates the noise into insights."*

---

## 🚀 Overview
**DataForge** is a production-ready, modular analytics engine designed to bridge the gap between raw CSV datasets and actionable intelligence. 

Traditional EDA (Exploratory Data Analysis) requires writing the same repetitive `pandas` and `matplotlib` code for every new project. DataForge automates this by providing an **interactive, no-code interface** that instantly generates:
* Statistical Profiling
* Missing Value Heatmaps
* Multivariate Correlation Analysis
* Distribution Logic (KDE vs Histograms)

Unlike standard dashboards, DataForge relies on a **decoupled architecture**. The core logic (`eda_functions.py`) is separated from the UI, allowing developers to import the engine into their own Jupyter Notebooks or ML pipelines.

---

## 📸 Interface & Features

### 1. 📂 Intelligent Data Profiling
Instantly view dataset shape, column data types, and a statistical summary (`.describe()`) without writing a single line of code.

### 2. 🔍 Missing Value Analysis
Automatically detects null values and generates a heatmap to visualize data gaps, helping you decide between imputation or dropping rows.

### 3. 📈 Automated Visualization Engine
* **Univariate:** Box plots for outlier detection and Distribution plots for skewness.
* **Bivariate:** Scatter matrices with regression lines to find trends.
* **Multivariate:** Interactive Correlation Heatmaps (Pearson/Spearman) to detect multicollinearity.

---

## 🛠️ Technical Architecture

```bash
DataForge-Analytics/
├── app.py                # The Streamlit Frontend Interface
├── eda_functions.py      # The "Brain": Modular Python functions for stats/plotting
├── requirements.txt      # Dependency Management
└── README.md             # Documentation