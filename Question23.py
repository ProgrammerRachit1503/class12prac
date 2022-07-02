import pandas as pd
dict1={'icode':['a21','b26','b35','c80','a30'],
      'item':['frock','cot','soft toy','baby socks','baby suit'],
      'dp':['2016-01-23','2015-09-23','2016-06-17','2014-10-16','2015-09-20'],
      'up':[700,5000,800,100,500],
      'disc':[10,25,10,7,5]}
item1=pd.DataFrame(dict1,index=[10,20,30,40,50])
#1
#print(item1)
#2
item1['c name']=pd.Series(['Godrej','P&G','Godrej','Tata','Godrej'],index=[10,20,30,40,50])
print('\n',item1)
#3
item1['qual']=pd.Series(['a+','a','b','a+','a'], index=[10,20,30,40,50])
print('\n',item1)
#4
item1=item1.assign(area=['west','east','east','north','west'])
print('\n',item1)
#5
acode=['123','456','123','345','123']
item1.insert(loc=5,column='acode',value=acode)
print('\n',item1)
#6
item1.insert(loc=3,column='color',value=['red','blue','green','red','orange'])
print('\n',item1)
