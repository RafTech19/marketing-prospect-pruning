# 📊 Marketing Performance Optimization through Prospect Pruning

**Final Project — Comprehensive Data Analytics Bootcamp (CODA RMT 015 · Group 3)**

A data-driven marketing analysis that identifies and eliminates low-performing 
prospect segments to improve conversion efficiency and reduce acquisition costs.

📎 [View Presentation](https://docs.google.com/presentation/d/12lX_AyWehxWUs_jzgzrQeyR4WXKcOrnD/edit?usp=sharing&ouid=108833759054259498252&rtpof=true&sd=true) · 📊 [View Dashboard](https://lookerstudio.google.com/reporting/d517a1b7-ed90-4e72-b852-8859b7be2316/page/kVhuF)

---

## 🎯 Project Objective

This project aims to optimize marketing acquisition costs through a **Prospect Pruning** 
strategy — systematically eliminating ineffective customer segments to drive a significant 
increase in conversion rate while maintaining budget efficiency.

> **Main Question:** What is the most effective method to identify unproductive customers 
> and determine the optimal pruning threshold that yields the most efficient increase 
> in conversion rate?

---

## 📐 SMART Framework

| | Goal |
|---|---|
| **S**pecific | Identify low-performing customer segments & estimate potential marketing cost savings |
| **M**easurable | Eliminate minimum 10% of low-performing prospects & calculate total AdSpend savings |
| **A**chievable | Conducted using historical data (demographics, campaign performance, engagement) via Python |
| **R**elevant | Strategic recommendations aligned with SDG 8 (Decent Work and Economic Growth) |
| **T**ime-bound | Completed within project timeline for timely and actionable business insights |

---

## 🚀 Business Impact

| Metric | Before | After (10% Pruning) |
|---|---|---|
| Conversion Rate | 87.65% | **90.53%** (+2.88%) |
| Total AdSpend | $40M | **$31.8M** (~20% saved) |
| Prospects Pruned | — | 1,632 (low-intent segments) |
| Savings per Lost Conv | — | **$6,557** |

---

## 🔍 Key Insights

### 👤 Demographics
- Conversion Rate remains consistently **above 85% across all demographic segments** 
  (age, gender, income) with minimal variance
- Demographics alone are **not reliable predictors** for identifying high-potential customers
- Strategy should shift focus toward **behavioral and engagement signals**

### 📣 Marketing Channel & Campaign
- **Referral** leads with the highest CR (88.31%) and largest volume (1,518 customers) — 
  trust-based strategies prove most effective for quality conversions
- **PPC** closely follows (88.28%), ideal for capturing immediate ready-to-buy intent
- **Conversion-type campaigns** achieve the highest efficiency at 93.36% CR
- **Retention campaigns** have the lowest volume (1,671) despite a stable 85.82% CR — 
  an untapped opportunity for maximizing Customer Lifetime Value (CLV)

### 💡 Top Conversion Drivers
- **Email Opens (8–9x):** Highest CR at 93.53% — email engagement frequency 
  directly scales conversion probability
- **AdSpend ($8,962–$9,997):** Peak investment levels deliver 93.00% CR — 
  marketing spend shows a linear positive correlation with conversions
- **Previous Purchases (3–4x):** Repeat buyers maintain 92.72% CR — 
  retention strategies significantly outperform new prospect acquisition

### ✂️ Pruning Analysis
- **Previous Purchases** is the #1 pruning signal — eliminating prospects with 
  0 transactions boosts CR to 90.53% with only 1,632 volume loss
- **Pages Per Visit** is the #2 signal — filtering users with <4 page views 
  raises CR to 90.39%, efficiently removing "window shoppers"
- **20% Pruning** shows diminishing returns — only +0.21% additional CR 
  but sacrifices 819 more leads, making 10% the optimal sweet spot
- Pruned prospects cost **~$850 more** in advertising than the average customer, 
  justifying their removal

---

## 💡 Recommendation (SMART Budgeting)

| | Strategy |
|---|---|
| **S**elective Pruning | Focus on 10% pruning of Previous Purchases to eliminate low-value segments without sacrificing significant conversion volume |
| **M**aximize Efficiency | Optimize budget toward segments with highest cost-efficiency (Savings per Lost Conv = $6,557) |
| **A**udience Prioritization | Prioritize high-intent audiences (3–4 Previous Purchases & 8–9 Email Opens) with proven CR >92% |
| **R**eallocate Budget | Shift the saved ~20% budget to channels/segments with the best conversion performance |
| **T**rack & Optimize | Conduct regular monitoring of CR, CPA, and engagement metrics to ensure strategy remains optimal |

---

## 🛠️ Tech Stack

`Python` · `PySpark` · `PostgreSQL (NeonDB)` · `Apache Airflow` · 
`Great Expectations` · `Looker Studio` · `SQLAlchemy`

---

## 🏗️ Data Pipeline
Kaggle API → PySpark (ETL) → NeonDB/PostgreSQL → Airflow (daily schedule) → Looker Studio

**Star Schema:** `dim_customer` · `dim_channel` · `dim_campaign_type` · `fact_marketing_performance`

**Data Validation (Great Expectations):**
- Unique CustomerID per row
- Valid campaign channel categories (Email, Social Media, PPC, Referral, SEO)
- Gender values restricted to authorized entries
- AdSpend column validated as float type
- Conversion column existence verified as primary target variable

---

## 👥 Team

| Name | Role |
|---|---|
| Zafirah Aida Adista | Data Analyst |
| Muhammad Rafli Febriyanto | Data Analyst |
| Muhamad Imam Ferdiansyah | Data Engineer |
