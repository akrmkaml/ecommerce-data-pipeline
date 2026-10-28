import sqlite3
import pandas as pd

print("1. Connecting to SQL Database...")
conn = sqlite3.connect("ecommerce.db")

# --- التقرير الأول: متوسط السعر لكل قسم (Category) ---
print("\n--- Average Price per Category ---")
query1 = """
    SELECT category, AVG(price) as avg_price, COUNT(id) as total_products
    FROM products
    GROUP BY category
    ORDER BY avg_price DESC
"""
df1 = pd.read_sql_query(query1, conn)
print(df1.to_string(index=False))

# --- التقرير الثاني: أغلى 5 منتجات (Premium Products) ---
print("\n--- Top 5 Most Expensive Products ---")
query2 = """
    SELECT title, price, category
    FROM products
    ORDER BY price DESC
    LIMIT 5
"""
df2 = pd.read_sql_query(query2, conn)
print(df2.to_string(index=False))

# --- التقرير الثالث: فلترة المنتجات اللي سعرها أعلى من 100 دولار ---
print("\n--- Products Over $100 ---")
query3 = """
    SELECT title, price
    FROM products
    WHERE price > 100
"""
df3 = pd.read_sql_query(query3, conn)
print(f"Found {len(df3)} products over $100.")

conn.close()