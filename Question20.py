import csv
import pandas as pd
d={'name':['Krish', 'Balram'],'roll':[21,22]}
df=pd.DataFrame(d)
print(df)
df.to_csv('S:\\Session 2021-22\\Class 12\\IP\\Practical file\\1.csv')
