# Write a menudriven program to extract data from dataframe
#a) Column  Wise  b)  Column  Wise  Series  object  (iteritems()).

import pandas as pd
import numpy as np

def colwise():
      for(col,colSeries)in df.iteritems():
            print('Column index:',col)
            print('containing:')
            print(colSeries)
def colseriesobj():
      for(col,colSeries)in df.iteritems():
            print('col index:',col)
            print('containing:')
            i=0
            for val in colSeries:
                  print('AT',i,'Position:',val)
                  i=i+1

data={'yr1':{'Qtr1':3500,'Qtr2':5600,'Qtr3':3300,'Qtr4':4500},
      'yr2':{'Qtr1':5500,'Qtr2':4600,'Qtr3':6700,'Qtr4':8900},
      'yr3':{'Qtr1':9000,'Qtr2':7800,'Qtr3':7800,'Qtr4':2200}}
df=pd.DataFrame(data)
print(df)
while 1:
      print("="*40)
      print("********Main	Menu*******")
      print("1 for extracting data columnwise")
      print("2 for extracting data columnwise series object")
      print("="*40)
      n=int(input("Enter your Choice(1,2): "))
      if n==1:
            print("extracting  data  columnwise ")
            colwise()
      elif n==2:
            print("extracting data columnwise series object ")
            colseriesobj()
      else:
            print("Your choice is Wrong")
      ch=input("Y/N : ")
      if ch=='n' or ch=='N':
            break
