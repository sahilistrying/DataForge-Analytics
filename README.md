# 📊 DataForge: Automated EDA & Analytics Platform

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> *"Data speaks, but only if you know how to listen. DataForge translates the noise into insights."*

---

## 👨‍💻 Why I Built This
**This project was born out of frustration.** As I worked on more data science problems, I realized I was rewriting the same initialization code—loading CSVs, checking for nulls, and plotting distributions—for every single project. It was repetitive and took time away from the actual modeling.

**DataForge** is my solution to that bottleneck. I wanted a tool that could handle the "boring" parts of data analysis instantly. This project also marks a personal milestone: it's my transition from writing isolated scripts in Jupyter Notebooks to building modular, full-stack data applications.

---

## 🚀 Overview
**DataForge** is a production-ready, modular analytics engine designed to bridge the gap between raw CSV datasets and actionable intelligence. 

Unlike standard dashboards, DataForge relies on a **decoupled architecture**. The core logic (\eda_functions.py\) is separated from the UI, allowing developers to import the engine into their own Jupyter Notebooks or ML pipelines.

### Key Capabilities
* **Intelligent Profiling:** Instantly detects data types and statistical moments.
* **Smart Visualization:** Dynamically chooses between KDE plots and Histograms based on skewness.
* **Interaction:** All charts are rendered using Plotly, allowing for zooming, panning, and hovering.

---

## ⚙️ How It Works
1.  **Ingestion:** The app accepts CSV uploads and converts them into a Pandas DataFrame.
2.  **Processing:** The \eda_engine\ cleans the data, infers data types (Numerical vs. Categorical), and calculates statistical summaries.
3.  **Rendering:** Streamlit's reactive framework listens for user inputs (e.g., "Show Outliers") and triggers Plotly to render interactive charts in real-time.

---

## ⚡ Getting Started
Want to see it in action? Follow these steps to run the app on your own machine.

### Prerequisites
* Python 3.8 or higher installed.

### Installation

1.  **Clone the repository**
    `ash
    git clone [https://github.com/sahilistrying/DataForge-Analytics.git](https://github.com/sahilistrying/DataForge-Analytics.git)
    cd DataForge-Analytics
    `

2.  **Install Dependencies**
    `ash
    pip install -r requirements.txt
    `

3.  **Launch the Application**
    `ash
    python -m streamlit run app.py
    `
    *The app will automatically open in your default web browser.*

---

## 🔮 Future Roadmap & Contributing
We have ambitious plans to make DataForge the standard for open-source EDA.

* [ ] **AI Insights:** Integrate OpenAI/Gemini API to provide text-based explanations of the data trends.
* [ ] **Report Generation:** Add a "Download PDF" button to export the entire analysis as a report.
* [ ] **SQL Support:** Allow direct connection to SQL databases instead of just CSV files.

### 🤝 Want to help?
Contributions are welcome! If you are interested in working on any of the features above, please open a PR. Let's build the future of accessible data science together.

---

<p align="center">
  <i>Built by Sahil. Focused on making Data Science accessible.</i>
</p>
