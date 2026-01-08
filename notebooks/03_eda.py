
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/cleaned/clean_superstore.csv')

df.groupby('category')['sales'].sum().plot(kind='bar')
plt.title('Sales by Category')
plt.show()

df.groupby('region')['profit'].sum().plot(kind='bar')
plt.title('Profit by Region')
plt.show()
