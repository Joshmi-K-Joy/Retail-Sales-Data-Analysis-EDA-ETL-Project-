
import pandas as pd

df = pd.read_csv('../data/raw/superstore.csv')

df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')

df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
df['profit'] = pd.to_numeric(df['profit'], errors='coerce')

df_clean = df.dropna(subset=['sales'])

df_clean.to_csv('../data/cleaned/clean_superstore.csv', index=False)
print("Cleaning complete. File saved.")
