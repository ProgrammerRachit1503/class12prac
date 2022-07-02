import pandas as pd
vend={'vname':['A','B','C','E','F'],
      'item':['chair','table','pen','eeraser','sketch pen'],
      'area':['east','west','south', 'SW','NE'],
      'qty':[30,45,23,12,100]}
vendor=pd.DataFrame(vend,index=[200,201,202,203,204])
#1
print(vendor)

#2
vendor.loc[205]=['g','sofa','east',15]
print('\n',vendor)
#3
vendor.loc[203]=['Amna','eraser','SW',12]
print('\n',vendor)
#4
vendor.iloc[3]=['Am','eraser','SW',23]
print('\n',vendor)
#5
print('\n',vendor.drop(203))
#6
vendor.drop(203, inplace=True)
print('\n',vendor)
#7
print('\n',vendor.drop([202,205]))
#8
print('\n',vendor.drop(vendor.index[2]))
#9
vendor.drop(vendor.index[[2,4]],inplace=True)
print('\n',vendor)
