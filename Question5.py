#Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
import pandas as pd

ds1 = pd.Series([200, 400, 600, 800, 1000])
ds2 = pd.Series([100, 300, 500, 700, 900])
print('Values of series ds1',ds1.values)
print('Values of series ds2',ds2.values)
print('='*85)
print('Arithmetic Operations')
ds3 = ds1 + ds2
print("Add two Series:",ds3.values)
ds4 = ds1 - ds2
print("Subtract two Series:",ds4.values)
ds5 = ds1 * ds2
print("Multiply two Series:",ds5.values)
ds6 = ds1 / ds2
print("Divide Series1 by Series2:",ds6.values)
