import pandas as pd

#read data from csv file in to a dataframe
df = pd.read_csv('expanded_sales_data.csv',encoding='utf-8')

print("displaying the info of the data set")
print(df.info())
