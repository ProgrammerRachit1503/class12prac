#Write a Pandas program to shows the attributes of series
import pandas as pd
import numpy as np
s1  =  pd.Series([6,6.9,5.9,2.6,5.7])
s2 = pd.Series([1,6,np.NaN])
s3 = pd.Series([], dtype='float64')

print('Values of the Series s1:',s1.values) 
print('index of the Series s1:',s1.index)
print('Size of the Series s1:',s1.size)
print('Number of bytes in s1:',s1.nbytes)
print('Check for emptyness in s1:', s1.empty)
print('Check for NaNs in s1:', s1.hasnans)
print('Dtype of the objects:',s1.dtype)
print('-'*65) 
print('Values of the Series s2:',s2.values)
print('index of the Series s2:',s2.index)
print('Size of the Series s2:',s2.size)
print('Number of bytes in s2:',s2.nbytes)
print('Check for emptyness in s2:',s2.empty)
print('Check  for  NaNs in s2:', s2.hasnans)
print('Dtype of  the objects:',s2.dtype)
print('-'*65)
print('Values of the Series s3:',s3.values)
print('index of the Series s3:',s3.index)
print('Size of the Series s3:',s3.size)
print('Number of bytes in s3:',s3.nbytes)
print('Check for emptyness in s3:',s3.empty)
print('Check for NaNs in s3:', s3.hasnans)
print('Dtype of the objects:',s3.dtype)
print('-'*65)
