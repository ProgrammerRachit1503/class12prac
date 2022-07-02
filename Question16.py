#Create multiline chart on common plot where three data range plotted on same chart. The data range(s) to be plotted are.
#data=[[5,25,45,20],[8,1,29,27],[9,29,27,39]]

import numpy as np
import matplotlib.pyplot as plt
data=[[5,36,40,10],[8,30,29,7],[9,29,39,49]]
x=np.arange(4)
plt.plot(x,data[0],color='b',label='range 1')
plt.plot(x,data[1],color='g',label='range 2')
plt.plot(x,data[2],color='r',label='range 3')
plt.legend(loc='upper left')
plt.title('Multi range line chart')
plt.xlabel('X')
plt.xlabel('Y')
plt.grid(True)
plt.show()
