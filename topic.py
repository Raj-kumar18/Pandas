import pandas as pd

df = pd.read_csv('expanded_sales_data.csv',encoding='utf-8',index_col=0)

print("display the shape of the data set")
print(f'Shape of the data set: {df.shape}')

print("-----------------------------------")
print("display the columns names of the data set")
print(f'Columns names of the data set: {df.columns}')