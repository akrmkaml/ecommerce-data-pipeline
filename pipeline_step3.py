import sqlite3
import pandas as pd
from google import genai

# 1. حط مفتاح جوجل بتاعك هنا
API_KEY = "YOUR_GEMINI_API_KEY_HERE"
client = genai.Client(api_key=API_KEY)

print("1. Extracting data from SQL for AI analysis...")
conn = sqlite3.connect("ecommerce.db")

# بنسحب البيانات اللي هنبعتها للـ AI
query = "SELECT category, AVG(price) as avg_price, COUNT(id) as total_products FROM products GROUP BY category"
df = pd.read_sql_query(query, conn)

# بنحول الجدول لنص عشان الـ AI يقراه
data_text = df.to_string(index=False)

conn.close()

# 2. نجهز الطلب (Prompt) للـ AI
print("2. Asking Gemini AI to write the business report...")
prompt = f"""
You are an expert Business Analyst. I extracted the following data from an e-commerce database:

{data_text}

Please write a short, professional Executive Summary (in English) for the business owner based on this data. 
Focus on:
- Which category is the most expensive on average?
- Which category has the highest number of products?
- Give 1 actionable recommendation based on these numbers.
"""

# 3. نبعت الطلب ونستلم الرد
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

# 4. نطبع التقرير
print("\n--- AI BUSINESS REPORT ---")
print(response.text)

# 5. نحفظ التقرير في ملف
with open("business_report.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("\nDone! Report saved to 'business_report.txt'")