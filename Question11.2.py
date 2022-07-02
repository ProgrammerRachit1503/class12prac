# Case Study 1
# Part 2:-Display the row labels  and column wise of Sales.
import pandas as pd
d = {2018:[110,130,115,118],
     2019:[205,165,175,190],
     2020:[115,206,157,179],
     2021:[118,198,183,169]}
sales=pd.DataFrame(d,index=['Kapil','Kamini','Shikhar','Mohini'])
#Display row labels
print("Row Lables:\n",sales.index)
print("---------------"*5,"\n")
#Display column lables
print("Column Lables:\n",sales.columns)
print("---------------"*5,"\n")
