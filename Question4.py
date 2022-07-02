#Write a Pandas program to create data series and then change the index of the series objects in any random order

import pandas as pd

s1 = pd.Series(data=[100,200,300,400,500],index=['a','b','c','d','e'])
print('-'*25)
print("Original Data")
print(s1)
s1=s1.reindex(index=['b','a','c','e','d'])
print('-'*25)
print("Reindex Data")
print(s1)
