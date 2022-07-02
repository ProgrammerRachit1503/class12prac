# Write a Python Program to create the dataframe with following values and perform head() & tail () Functions on it.
import pandas as pd
import numpy as np
d  =  {'Name':pd.Series(['Tom','Jerry','Rachit','Vishu','Prerak','Raghav','Jackie']),
       'Age':pd.Series([15,16,17,13,13,19,23]),
       'Rating':pd.Series([4,3.5,5,1.5,4.9,4.6,2.8])}
df = pd.DataFrame(d)
print('-'*40)
print("Our data frame is:")
print(df)
print('-'*40)
print("The first two rows of the data frame is:")
print(df.head(2))
print('-'*40)
print("The last two rows of the data frame is:")
print(df.tail(2))
print('-'*40)
