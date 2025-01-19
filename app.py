import pandas as pd

#read data from csv file in to a dataframe
# df = pd.read_csv('expanded_sales_data.csv',encoding='utf-8')
# df = pd.read_excel('Sample - Superstore.xls')
df = pd.read_json('sample_data.json')
print(df) 

#gcsfs is a library for google cloud storage
# import gcsfs
# fs = gcsfs.GCSFileSystem()
# df = pd.read_json(fs.open('gs://my-bucket-name/my-file-name.json'))