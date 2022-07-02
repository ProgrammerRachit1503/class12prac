#Write a Pandas program to find out the biggest and smallest
#three areas from a given series that  stores  the  areas  of  some  states in km^2.

import pandas as pd

ser= pd.Series([3466,980,450,67892,34677,7892,65711,\
                68291,20136,25723,236,2189,345,265610])
print(ser.values)
print('-'*50)
print('Top 3 Biggest area are:-')
print(ser.sort_values().tail(3))
print('Top 3 Smallest area are:-')
print(ser.sort_values().head(3))
