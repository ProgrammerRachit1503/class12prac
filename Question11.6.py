#case study 1
#6. Display the first two columns of Sales.
import pandas as pd
d = {2018:[110,130,115,118],
     2019:[205,165,175,190],
     2020:[115,206,157,179],
     2021:[118,198,183,169]}
sales=pd.DataFrame(d,index=['Kapil','Kamini','Shikhar','Mohini'])
print("First two columns")
print(sales[[2018,2019]])
