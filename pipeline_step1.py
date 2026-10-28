import requests
import pandas as pd
import sqlite3
import time

# 1. محاولة جلب البيانات من FakeStoreAPI
url_primary = "https://fakestoreapi.com/products"
# 2. رابط بديل (DummyJSON) لو الأول فشل
url_backup = "https://dummyjson.com/products?limit=100"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print("1. Fetching data from API (Trying Primary)...")
try:
    # بنجرب الموقع الأول
    response = requests.get(url_primary, headers=headers, timeout=10)
    response.raise_for_status() # لو فيه مشكلة في السيرفر هيرمي إيرور
    data = response.json()
    print("   -> Success from FakeStoreAPI!")
except Exception as e:
    print(f"   -> Primary API failed ({e}). Switching to Backup API...")
    # لو فشل، بنجيب من الموقع التاني
    response = requests.get(url_backup, headers=headers, timeout=10)
    response.raise_for_status()
    # الموقع التاني بيرجع الداتا جوه مفتاح اسمه products
    data = response.json()['products']
    print("   -> Success from DummyJSON!")

# --- من هنا الكود زي ما هو (تجهيز الداتا وحفظها في SQL) ---
df = pd.DataFrame(data)

# بنختار الأعمدة المهمة (الأسماء ممكن تختلف شوية بين الموقعين)
# في FakeStoreAPI: rating عبارة عن dict
# في DummyJSON: rating هو رقم عادي
if 'rating' in df.columns and isinstance(df['rating'].iloc[0], dict):
    df['rating_rate'] = df['rating'].apply(lambda x: x.get('rate', 0))
    df = df.drop('rating', axis=1)

# بنختار الأعمدة اللي محتاجينها
cols_to_keep = ['id', 'title', 'price', 'category']
if 'rating_rate' in df.columns:
    cols_to_keep.append('rating_rate')

df = df[cols_to_keep]

print("Data fetched successfully! Here is a preview:")
print(df.head())

# 2. حفظ الداتا في قاعدة بيانات SQL
print("\n2. Saving data to SQL Database...")
conn = sqlite3.connect("ecommerce.db")
df.to_sql("products", conn, if_exists="replace", index=False)
conn.close()
print("Done! Data saved to 'ecommerce.db'")