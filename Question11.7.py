# Case Study 1
# Part 7:-Change the DataFrame Sales such that it becomes its transpose.
import pandas as pd
d = {2018:[110,130,115,118],
     2019:[205,165,175,190],
     2020:[115,206,157,179],
     2021:[118,198,183,169]}
sales=pd.DataFrame(d,index=['Kapil','Kamini','Shikhar','Mohini'])
print("Original :-")
print(sales)
print("-"*40,"\n")
print("Transpose:-")
print(sales.T)
