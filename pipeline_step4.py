import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="E-commerce Analytics", layout="wide")
st.title("🛍️ E-commerce Market Analyzer")
st.markdown("Automated Data Pipeline: API -> SQL -> AI Report.")

# 1. الاتصال بقاعدة البيانات
conn = sqlite3.connect("ecommerce.db")

# 2. عرض الإحصائيات العامة
df = pd.read_sql_query("SELECT * FROM products", conn)
col1, col2, col3 = st.columns(3)
col1.metric("Total Products", len(df))
col2.metric("Total Categories", df['category'].nunique())
col3.metric("Max Price", f"${df['price'].max():,.2f}")

st.divider()

# 3. عرض الرسم البياني (متوسط السعر لكل قسم)
st.subheader("Average Price by Category")
query_avg = "SELECT category, AVG(price) as avg_price FROM products GROUP BY category"
df_avg = pd.read_sql_query(query_avg, conn)
st.bar_chart(df_avg, x="category", y="avg_price")

# 4. عرض أغلى المنتجات
st.subheader("Top 5 Most Expensive Products")
query_top = "SELECT title, price, category FROM products ORDER BY price DESC LIMIT 5"
df_top = pd.read_sql_query(query_top, conn)
st.dataframe(df_top, width='stretch')

conn.close()

# 5. عرض تقرير الذكاء الاصطناعي
st.divider()
st.subheader("🤖 AI Business Report")
try:
    with open("business_report.txt", "r", encoding="utf-8") as f:
        report_text = f.read()
    st.info(report_text)
except FileNotFoundError:
    st.warning("AI Report not found. Please run pipeline_step3.py first.")