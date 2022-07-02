import matplotlib.pyplot as plt
import numpy as np
range1=np.arange(0,10,0.1)
sin=np.sin(range1)
cos=np.cos(range1)
tan=np.tan(range1)
plt.plot(range1,sin,label='sin',color='red')
plt.plot(range1,cos,label='cos',color='blue')
plt.plot(range1,tan,label='tan',color='purple')
plt.xlabel("Range")
plt.ylabel('Values')
plt.legend(loc=5)
plt.grid(True)
plt.ylim(-5,5)
plt.xlim(0,10)
plt.show()
