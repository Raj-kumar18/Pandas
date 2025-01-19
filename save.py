import pandas as pd
from openpyxl.workbook import Workbook   
data = {
    "OrderID": [1001, 1002, 1003, 1004, 1005],
    "ProductName": ["Shoes", "T-Shirt", "Jacket", "Pants", "Socks"],
    "Quantity": [2, 1, 1, 2, 6],
    "Price": [50, 20, 80, 40, 10],
    "Total": [100, 20, 80, 80, 60],
    "Date": ["2025-01-15", "2025-01-16", "2025-01-17", "2025-01-18", "2025-01-19"],
    "CustomerID": ["C001", "C002", "C003", "C004", "C005"]
}

df = pd.DataFrame(data)
# print(df)
# df.to_csv('output.csv',index=False)
# df.to_excel('output.xlsx',index=False)
df.to_json('output.json',index=False)