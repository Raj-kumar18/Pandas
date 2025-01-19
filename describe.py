import pandas as pd

data={
    "Name" : ["Raj","Ravi","Rahul","Rohit","Ramesh","Rajesh"],
    "Age" : [20,21,22,23,24,25],
    "Gender" : ["M","M","M","M","M","M"],
    "Salary" : [10000,20000,30000,40000,50000,60000],
    "Date" : ["2025-01-15","2025-01-16","2025-01-17","2025-01-18","2025-01-19","2025-01-20"],
    "EmployeeID" : ["E001","E002","E003","E004","E005","E006"],
    "Company" : ["ABC","DEF","GHI","JKL","MNO","PQR"],
    "State" : ["A","B","C","D","E","F"],
    "City" : ["G","H","I","J","K","L"],
    "Country" : ["M","N","O","P","Q","R"],
    "Pincode" : [123456,234567,345678,456789,567890,678901],
    "Mobile" : [1234567890,2345678901,3456789012,4567890123,5678901234,6789012345]
}

df = pd.DataFrame(data)
print("display summary statistics of numeric columns")
print(df.describe())