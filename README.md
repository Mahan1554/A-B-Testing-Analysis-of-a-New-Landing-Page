# A/B Testing Analysis of a New Landing Page

This project analyzes whether the new landing page design leads to a statistically significant improvement in user conversion compared to the old page using A/B Testing.

## 📌 Objective

Determine whether the new landing page results in a higher conversion rate than the old landing page using hypothesis testing.

## 🎯 Business Problem

The company wants to increase conversions (e.g., purchases or signups). To achieve this, they launched a new landing page and ran an A/B experiment to evaluate if it performs better than the existing one.

## 🧠 Dataset Overview

| Column Name   | Description |
|---------------|-------------|
| `user_id`     | Unique identifier for each user |
| `timestamp`   | Time the user visited the website |
| `group`       | Whether the user is in the control or treatment group |
| `landing_page`| The version of the landing page shown (old_page or new_page) |
| `converted`   | Whether the user converted (1) or not (0) |

## 📊 Analysis & Methods

- Data Cleaning & Preprocessing
- Exploratory Data Analysis
- Visualizations:
  - Average conversion rate by group
  - Distribution of received pages
  - Conversion histograms
  - Time-series plots of daily and 7-day rolling conversions
  - Z-test rejection region visualization
- Hypothesis Testing using Z-Test
  - Null Hypothesis: Conversion rate of new page = old page
  - Alternative Hypothesis: Conversion rate of new page ≠ old page

## 🔬 Key Results

- **Z-Score:** -1.3109  
- **P-Value:** 0.1899  
- **95% Confidence Interval:** (-0.00394, 0.00078)  
- **Observed Effect:** -0.00157  
- **Minimum Detectable Effect (MDE):** 0.01  
- **Result:** Not statistically or practically significant

## 🌐 Streamlit App
[View the A/B Testing Analysis App](https://abtestresult.streamlit.app)
An interactive Streamlit interface was built showcasing:
- Business Problem and Objective
- Dataset Description
- Visualizations
- Hypothesis Test Results
- Conclusion & Interpretation


