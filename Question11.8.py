#Case Study 1
#8. Display the sales made by all sales persons in the year 2018.

import pandas as pd
d = {2018:[110,130,115,118],
     2019:[205,165,175,190],
     2020:[115,206,157,179],
     2021:[118,198,183,169]}
sales=pd.DataFrame(d,index=['Kapil','Kamini','Shikhar','Mohini'])
print(sales)
print("-"*40,"\n")
#Method 1
print(sales[2018])
print("-"*40,"\n")
#Method 2
print(sales.loc[:,2018])
