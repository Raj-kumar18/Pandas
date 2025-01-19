import pandas as pd

#read data from csv file in to a dataframe
#head() -> first 5 rows by default
#tail() -> last 5 rows by default
#sample() -> random rows by default
#describe() -> summary statistics of numeric columns
df = pd.read_csv('expanded_sales_data.csv',encoding='utf-8')
print("display first 10 rows")
print(df.head(10))

print("-----------------------------------")
print("display last 10 rows")
print(df.tail(10))

print("-----------------------------------")
print("display random 10 rows")
print(df.sample(10))