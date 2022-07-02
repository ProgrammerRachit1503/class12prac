# Write a program to plot line graph using (subplot )

import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[5,10,15,20]
z=[10,12,14,16]
w=[1,2,4,8]
plt.subplot(3,1,1)
plt.plot(x,y,'g',linestyle="--", linewidth=5)
plt.title(" Students participating for ART")
plt.xlabel("CLASS", fontsize="8",color="red")
plt.ylabel("NO OF STUDENTS PARTICIPATING", fontsize="6", color="red")
plt.subplot(3,1,2)
plt.plot(x,z,'m',linestyle="--", linewidth=5)
plt.xlabel("CLASS", fontsize="8",color="green")
plt.subplot(3,1,3)
plt.plot(x,w,'b',linestyle="--", linewidth=5)
plt.grid(True)
plt.show()
