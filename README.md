# Retail Sales Performance Analysis using Python

## 📌 Project Overview

This project focuses on performing **end-to-end data analytics** on a retail sales dataset to derive actionable business insights. The analysis starts from raw data ingestion and validation, followed by data cleaning, transformation, and exploratory data analysis (EDA) using Python.

The goal of the project is to understand **sales performance, profitability patterns, discount impacts, and regional trends**, which can help businesses improve revenue and decision-making.

---

## 🧠 Business Problem

Retail organizations generate large volumes of transactional data, but without proper analysis, this data cannot effectively support decision-making.

This project aims to answer questions such as:

* Which products, categories, and regions drive sales and profit?
* Are there loss-making transactions and what causes them?
* How do discounts affect profitability?
* Are there data quality issues that could impact analysis accuracy?

---

## 🛠️ Tools & Technologies

* **Programming Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn
* **Environment:** Jupyter Notebook
* **Dataset Type:** Retail transactional sales data

---

## 📂 Project Structure

```
Retail_Sales_Analytics_Project/
│
├── data/
│   ├── raw/
│   │   └── superstore_raw.csv
│   └── cleaned/
│       └── clean_superstore.csv
│
├── notebooks/
│   ├── 01_data_validation.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_exploratory_data_analysis.ipynb

```

---

## 🔍 Step 1: Data Validation

Initial checks were performed to understand data quality and structure:

* Verified column data types (dates, numeric, categorical)
* Identified missing values
* Checked for negative sales and profit values
* Reviewed business relevance of columns

✔ **Outcome:** Multiple data quality issues were identified, including missing sales values and negative profit records.

---

## 🧹 Step 2: Data Cleaning & Preparation

Based on validation findings, the following actions were taken:

* Converted numeric columns (`sales`, `profit`) from object to numeric types
* Handled missing values in sales data
* Ensured date columns were in proper datetime format
* Retained negative profit values as they represent genuine business losses

✔ **Final Clean Dataset Shape:** **48,660 rows × 21 columns**

---

## 📊 Step 3: Exploratory Data Analysis (EDA)

EDA was conducted to uncover patterns and trends:

* Sales and profit distribution analysis
* Category and sub-category performance evaluation
* Regional and market-level sales trends
* Discount vs profit impact analysis
* Identification of loss-making transactions

✔ Visualizations were used extensively to support insights.

---

## 📈 Key Insights

* A significant number of transactions resulted in negative profit, highlighting pricing or discounting inefficiencies
* High discounts were strongly correlated with lower profitability
* Certain categories contributed high sales volume but low profit margins
* Regional performance varied significantly, indicating potential for targeted strategies

---

## ✅ Conclusion

This project successfully demonstrates the complete **Python-based data analytics lifecycle**, from raw data validation to insight generation. The analysis provides meaningful business insights that can support strategic retail decisions related to pricing, discounting, and regional focus.

