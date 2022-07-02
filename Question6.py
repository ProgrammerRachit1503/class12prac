#Write a Python Program to create the dataframe with following values and perform attributes of dataframe on it.
import pandas as pd
data  =  {  'name':  ['Mohak',  'Rajesh',  'Freya',  'Aditya','Anika'], 
            'year':  [2012,  2012,  2013,  2014, 2014],
            'score': [10, 22, 11, 32, 23],
            'catches': [2, 2, 3, 3, 3] }
df = pd.DataFrame(data, columns= ['name','year','score','catches'])
print(df)
print('indexes of dataframe:',df.index)
print('columns of dataframe:',df.columns)
print('size of dataframe:',df.size)
print('shape of dataframe:',df.shape)
print('axes of dataframe:',df.axes)
