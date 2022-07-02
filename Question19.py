import pandas as pd
df=pd.read_csv('S:\\Session 2021-22\\Class 12\\IP\\Practical file\\Marks.csv',\
               names=['Name','Marks1','Marks2','Marks3'])
print('DataFrame after fetching data from csv file')
print(df)
df['Total']=df['Marks1']+df['Marks2']+df['Marks3']
df['AvgMarks']=df['Total']/3
print("Dataframe after Calculation")
print(df)
