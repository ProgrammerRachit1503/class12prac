# Display the dimensions, shape, size and values of Sales
import pandas as pd
d = {2018:[77000,64000,85000,90000],
     2019:[20000,98900,30000,60000],
     2020:[20000,0,10000,20000],
     2021:[30000,40000,60000,70000]}
sales=pd.DataFrame(d,index=['Kapil','Kamini','Shikhar','Mohini'])
print(sales)
#Display row lables
print("Row Lables:\n",sales.index)
print("-------------------------------\n")
#Display column lables
print("Column Lables:\n",sales.columns)
print("-------------------------------\n")
print("-------------------------------") 
print(sales.dtypes)
print("-------------------------------")
print("Dimensions:",sales.ndim)
print("Shape:",sales.shape)
print("Size:",sales.size)
print("Values:",sales.values)
