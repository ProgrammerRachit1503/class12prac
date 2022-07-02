import pandas as pd
import numpy as np
dict1={'icode':['a21','b26','b35','c80','a30'],
      'item':['frock','cot','soft toy','baby socks','baby suit'],
      'dp':['2016-01-23','2015-09-23','2016-06-17','2014-10-16','2015-09-20'],
      'color':['red','blue','green','red','orange'],
      'up':[700,5000,800,100,500],
      'disc':[10,25,10,7,5],
      'acode':['123','456','123','345','123'],
      'vname':['Godrej','P&G','Godrej','Tata','Godrej'],
      'qual':[np.nan,np.nan,np.nan,np.nan,np.nan],
      'area':['west','east','east','north','west']}
 
item1=pd.DataFrame(dict1,index=[10,20,30,40,50])
#1
print(item1)
#2
del item1['qual']
print('\n',item1)
#3b
print('\n',item1.pop('acode'))
#4a
print('\n',item1.drop(axis=1,labels=['vname']))
#7a
print("\n",item1.drop(axis=1, labels=['color','area']))
#7b
print("\n",item1.drop(columns=['color','area']))
#8
del item1['color']
del item1['area']
print('\n',item1)
