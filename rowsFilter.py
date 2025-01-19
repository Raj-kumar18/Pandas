import pandas as pd

#read data from csv file in to a dataframe
df = pd.read_csv('expanded_sales_data.csv',encoding='utf-8')
print(df)

#filter data based on condition
print("filter data based on condition")
heighPrice = df[df["Price"] >= 50]
print(heighPrice)

print("filter rows Price > 50 and Quantity > 2")
filterData = df[(df["Price"] >=50) & (df["Quantity"] > 2)]
print(filterData)



#using or operator
print("filter rows Price > 50 or Quantity > 2")
filter_orData = df[(df["Price"] >=50) | (df["Quantity"] > 2)]
print(filter_orData)