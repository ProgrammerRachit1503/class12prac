#Q1
import pandas as pd
dict1={'icode':['a21','b26','b35','c80','a30'],
'item':['frock','cot','soft toy','baby socks','baby suit'],
'dp':['2016-01-23','2015-09-23','2016-06-17','2014-10-16','2015-09-20'],
'up':[700,5000,800,100,500],
'disc':[10,25,10,7,5]}
item1=pd.DataFrame(dict1,index=[10,20,30,40,50])
print(item1)
#Q2
print(item1.loc[30])
#Q3
print(item1.loc[[20,40]])
#Q4(a)
print(item1.iloc[2])
#Q4(b)
print(item1.iloc[[1,3]])
#Q5a
print(item1.item)
#Q5b
print(item1['item'])
#Q6
print(item1[['item','up']])
#Q7a
print(item1.head(3))
#Q7b
print(item1[0:3])
'''Q8 Write code to display the details of itemcode A21, C80 and A30
using their default indexes.'''
print(item1.iloc[[0,3,4]])
#Q9 Write code to display the last 4 records from the data frame.
print(item1.tail(4))
#Q10 Write code to display the unitprice and discount of items B26 and C80.
print(item1.loc[[20,40],['up','disc']])
#Q11. Write code to display 2nd
# to 5th record (both inclusive)( they are the default index).
print(item1.iloc[2:6])
#Q12
print(item1.iloc[4])
#Q13
print(item1.loc[[20,40]])
#14
print(item1.iloc[1:4:2])
