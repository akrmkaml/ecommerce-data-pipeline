# 🛍️ End-to-End E-commerce Data Pipeline

An automated data pipeline that extracts product data from a REST API, stores it in a SQL database, performs SQL-based analysis, generates an AI business report (using Google Gemini), and displays everything in an interactive Streamlit dashboard.

## 🚀 Architecture & Workflow
1. **Data Extraction (`pipeline_step1.py`):** Fetches product data from an external API (with fallback handling) using `requests`.
2. **Data Storage (`pipeline_step1.py`):** Stores the cleaned data into a local SQLite database (`ecommerce.db`) using `sqlite3`.
3. **Data Analysis (`pipeline_step2.py`):** Runs advanced SQL queries (Grouping, Aggregations, Filtering) and loads results into Pandas DataFrames.
4. **AI Reporting (`pipeline_step3.py`):** Sends the SQL insights to the Google Gemini API to automatically generate a professional Executive Summary for business owners.
5. **Interactive Dashboard (`pipeline_step4.py`):** A Streamlit web application displaying KPIs, dynamic bar charts, and the AI-generated report.

## 🛠️ Tech Stack
- **Language:** Python 3.12
- **Libraries:** Pandas, Requests, Streamlit, Google GenAI
- **Database:** SQLite
- **AI:** Google Gemini API

## ⚙️ How to Run
1. Clone the repository.
2. Install requirements: `pip install pandas requests streamlit google-genai`
3. **Important:** Open `pipeline_step3.py` and replace `"YOUR_GEMINI_API_KEY_HERE"` with your actual Google Gemini API key.
4. Run the pipeline: `python pipeline_step1.py` then `python pipeline_step3.py`.
5. Launch the Dashboard: `streamlit run pipeline_step4.py`