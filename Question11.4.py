# Case Study 1
# Part 4:-Display the dimensions, shape, size and values of Sales.
import pandas as pd
d = {2018:[110,130,115,118],
     2019:[205,165,175,190],
     2020:[115,206,157,179],
     2021:[118,198,183,169]}
sales=pd.DataFrame(d,index=['Kapil','Kamini','Shikhar','Mohini'])
print("Dimensions:",sales.ndim)
print("Shape:",sales.shape)
print("Size:",sales.size)
print("Values:",sales.values)
