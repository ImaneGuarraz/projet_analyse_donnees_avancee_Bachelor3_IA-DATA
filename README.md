# projet_analyse_donnees_avancee_Bachelor3_IA-DATA
Comment transformer un dataset marketing en un système décisionnel capable d’éclairer la segmentation, le ciblage, la performance campagne et la feuille de route analytique de l’entreprise ?

LIEN DATASET : https://www.kaggle.com/datasets/rodsaldanha/arketing-campaign

LIEN CANVA : https://canva.link/sd1hpyy8s0bgec0 

🚀 📊 Advanced Marketing Analytics
Decision Intelligence • Segmentation • Scoring • BI
<p align="center"> <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python"> <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-orange?style=for-the-badge&logo=pandas"> <img src="https://img.shields.io/badge/Scikit--Learn-ML-yellow?style=for-the-badge&logo=scikit-learn"> <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge"> </p>
🎯 Project Overview

This project transforms a marketing dataset into a decision intelligence system designed to support business strategy.

The goal is to move from raw data to actionable insights, enabling:

smarter customer segmentation
optimized campaign targeting
improved marketing ROI
predictive scoring for decision-making
🧠 Key Business Question

How can we turn marketing data into a decision system that improves segmentation, targeting, and campaign performance?

📊 Dataset Description

The dataset contains customer-level information including:

socio-demographic data (age, income, education)
purchasing behavior (product spending, frequency)
marketing interactions (campaign responses)

🎯 Target variable: Response (customer reaction to last campaign)

Project Pipeline

Mermaid : 

flowchart LR
A[Raw Data] --> B[Data Cleaning]
B --> C[Feature Engineering]
C --> D[Exploratory Analysis]
D --> E[Segmentation]
E --> F[Modeling & Scoring]
F --> G[Dashboard & Insights]
G --> H[Business Recommendations]

Data Analysis

The exploratory analysis highlights key patterns:

Strong relationship between income and spending
Customers with higher spending are more likely to respond
Recency plays a critical role in engagement
Past campaign acceptance is a strong predictor of future behavior

Customer Segmentation

Customers were segmented using clustering techniques into distinct groups:

💎 High-value customers (VIP)
🔁 Regular customers
🚀 High-potential customers
⚠️ Low-value customers

This segmentation enables targeted marketing strategies.

📈 Key Metrics (KPI)

The project introduces business-oriented KPIs:

Campaign response rate
Average customer value
Segment performance
Customer scoring index

These indicators support data-driven decision-making.

🤖 Predictive Modeling

A machine learning model was developed to predict customer response.

✔️ Features used:
Income
Total spending
Recency
Campaign engagement
🎯 Output:
Propensity score (probability of response)

👉 This allows:

smarter targeting
cost reduction
ROI optimization
📊 Dashboard

An interactive dashboard (Streamlit) was built to:

monitor KPIs
explore customer segments
analyze campaign performance
identify high-value targets
🧪 Analytical Robustness

The analysis includes validation steps:

multicollinearity checks (VIF)
correlation analysis
outlier sensitivity
model evaluation

This ensures reliability and consistency of results.

⚙️ Industrialization

The project is structured as a reproducible pipeline:

data preprocessing
feature engineering
modeling
scoring

The system can be updated with new data and integrated into a CRM or BI tool.

💡 Business Recommendations

Key strategic insights:

🎯 Prioritize high-value and high-propensity customers
💰 Optimize marketing spend on responsive segments
🔁 Reactivate inactive but high-income customers
📊 Implement continuous KPI monitoring
🛠️ Tech Stack
Python
Pandas / NumPy
Matplotlib / Seaborn
Scikit-learn
Statsmodels
Streamlit

🚀 How to Run

pip install -r requirements.txt
streamlit run app.py

📁 Project Structure

├── data/
├── notebook/
├── app.py
├── requirements.txt
└── README.md

👥 Authors
Olympe DOTSU
Imane GUARRAZ

Final Insight

This project demonstrates how data can be transformed into a strategic asset, enabling companies to move from intuition to data-driven decision making.
