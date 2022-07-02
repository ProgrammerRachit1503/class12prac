# Write  a  Python  Program  to  create  the  dataframe  and selecting rows/column  using  loc  and  iloc  function.
import pandas as pd
data={'State':['Andhra','odisha','bihar','jharkhand','W.B'],
      'Toys':[400,500,600,1003,50000],
      'Books':[34999,45999,9998,59994,99975],
      'Uniform':[200,600,700,500,600],
      'Shoes':[500,500,799,800,465] }
df=pd.DataFrame(data,columns=['State','Toys','Books','Uniform','Shoes'])
print(df)
print('-'*80)
print('A. Show data of Toys Column')
print(df['Toys'])
print('-'*80)
print('B. Show data of First 3 rows Toys and Book columns (using loc)')
print(df.loc[0:2,['Toys','Books']])
print('-'*80)
print('C. Show data of First 2 rows State,Toys and Books columns (using iloc)')
print(df.iloc[0:2,0:3])
