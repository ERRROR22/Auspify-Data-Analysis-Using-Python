# Auspify Technologies - Data Analysis Using Python Internship

## 📌 Project Overview
This repository contains the complete 4-week practical data analysis project submitted for the **Data Analysis Using Python Internship Program** at **Auspify Technologies**. The project involves end-to-end data processing, exploratory data analysis (EDA), trend identification, and business intelligence reporting on the Netflix Movies & TV Shows dataset.

---

## 📁 Repository & Folder Structure

```text
├── Dataset.csv                                # Raw Netflix dataset provided for internship
├── README.md                                  # Complete project documentation & overview
│
├── Task_1_Data_Cleaning/
│   ├── task1_data_cleaning.py                 # Data cleaning, null handling & standardization script
│   └── netflix_cleaned.csv                    # Cleaned and processed dataset
│
├── Task_2_Content_Type_Analysis/
│   ├── task2_content_type_analysis.py         # Script analyzing Movies vs TV Shows distribution
│   └── content_type_distribution.png          # Visualizations (Bar chart & Donut chart)
│
├── Task_3_Country_Analysis/
│   ├── task3_country_analysis.py              # Geographic aggregation & top content producers script
│   └── top_10_countries.png                   # Top 10 content producing countries chart
│
├── Task_4_Trend_Analysis/
│   ├── task4_trend_analysis.py                # Time-series analysis of release trends over years
│   └── yearly_release_trend.png               # Production growth & decline trend visualization
│
├── Task_5_Rating_Genre_Analysis/
│   ├── task5_rating_genre_analysis.py         # Audience ratings & genre distribution script
│   └── rating_and_genre_distribution.png      # Rating breakdown & Top 10 genres chart
│
└── Task_6_Business_Insights_Report/
    ├── task6_business_insights_report.py      # End-to-end Executive BI Dashboard generator
    └── executive_bi_dashboard.png             # Consolidated 4-panel business dashboard
```

---

## 🛠️ Tech Stack & Requirements
- **Language**: Python 3.8+
- **Libraries Used**:
  - `pandas` (Data Manipulation & Preprocessing)
  - `numpy` (Numerical Computations)
  - `matplotlib` (Core Visualizations)
  - `seaborn` (Statistical Dashboards)

### Installation
To install the required dependencies, run:
```bash
pip install pandas numpy matplotlib seaborn
```

---

## 🚀 Tasks Breakdown & Key Findings

1. **Task 1: Netflix Data Cleaning & Preparation**
   - Cleaned string whitespaces, handled missing values, standardized content categories (`Type`, `Rating`), and extracted structured date & duration fields.

2. **Task 2: Content Type Analysis**
   - Netflix library consists of approximately **69.7% Movies** (6,126 titles) and **30.3% TV Shows** (2,664 titles).

3. **Task 3: Country-Wise Content Analysis**
   - The **United States** leads in total production, followed closely by **India** and the **United Kingdom**, showcasing rapid regional catalog growth.

4. **Task 4: Trend Analysis by Release Year**
   - Content production grew exponentially from 2014, reaching its peak around 2018–2020 as Netflix scaled its original streaming titles globally.

5. **Task 5: Content Rating & Genre Analysis**
   - **TV-MA** and **TV-14** are the dominant content ratings, targeting mature and young adult audiences. International Movies, Dramas, and Comedies form the bulk of genres.

6. **Task 6: Business Intelligence & Executive Dashboard**
   - Comprehensive multi-panel BI report providing strategic recommendations on catalog retention, regional content acquisition, and audience targeting.

---

## 👨‍💻 Author & Intern Details

- **Intern Name**: Ritik Sharma
- **Internship Track**: Data Analysis Using Python
- **Organization**: Auspify Technologies
- **Submission Date**: October 2026

---
*Created with dedication for Auspify Technologies Internship Program.*
