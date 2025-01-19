import pandas as pd

df = pd.read_csv('expanded_sales_data.csv',encoding='utf-8')

print("sample data")
print(df)

# print("ProductName (singlw column) retun series")
# print(df['ProductName'])

#selecting multiple columns
subset = df[['ProductName','Quantity']]
print(subset)