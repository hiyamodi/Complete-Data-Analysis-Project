import pandas as pd
import matplotlib.pyplot as plt
import os

# --- STEP 0: SETUP ---
# Create folders if they don't exist
os.makedirs('visualizations', exist_ok=True)

# --- STEP 1: LOAD DATA ---
# Looking inside the 'data' folder
try:
    df = pd.read_csv('data/sales_data.csv')
    print("Step 1: Data loaded from 'data/sales_data.csv'")
except FileNotFoundError:
    print("Error: Please make sure 'sales_data.csv' is inside the 'data' folder.")
    exit()

# --- STEP 2: CLEAN DATA ---
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')
print("Step 2: Data cleaned and sorted.")

# --- STEP 3: ANALYSIS ---
product_perf = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
region_perf = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
print("Step 3: Metrics calculated.")

# --- STEP 4: VISUALIZATIONS (Using Matplotlib Only) ---

# Chart 1: Product Performance (Bar Chart)
plt.figure(figsize=(10, 6))
product_perf.plot(kind='bar', color='#3498db', edgecolor='black')
plt.title('Total Revenue by Product Category', fontsize=14)
plt.xlabel('Product', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visualizations/product_sales.png')
plt.close()

# Chart 2: Regional Share (Pie Chart)
plt.figure(figsize=(8, 8))
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99'] # Custom color palette
plt.pie(region_perf, labels=region_perf.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Sales Distribution by Region', fontsize=14)
plt.savefig('visualizations/regional_share.png')
plt.close()

print("Step 4: Visualizations saved to 'visualizations/' folder.")
print("\n--- Project Pipeline Complete ---")