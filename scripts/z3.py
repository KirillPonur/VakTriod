import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter 
fig = plt.figure() 
ax = fig.add_subplot(111) 

x=np.array([17.2,13,11.8,11,10.2,9.6,8.9,8.3,7.8,7.4,7.2,6.8,6.6,6.4,6.1,5.8,5.7,5.5]) 
y=np.array([0,0.2,0.4,0.7,1.2,1.7,2.5,3.4,4.2,5,5.5,6.3,7,7.7,8.4,9,9.4,10]) 
plt.errorbar(x, y, xerr=0.1, yerr=0.1, c='navy', marker='.', ms=5, fmt='o')
 
ax.plot(-x,y,'ko', color = "orangered", markersize=4) 

x=np.array([17,10.2,8.8,8.2,7.6,7.1,6.5,6.1,5.8,5.2,5,4.7,4.4,4.1,3.9,3.7,3.4,3.2,3,2.8,2.6]) 
y=np.array([0,0.1,0.2,0.4,0.5,0.8,1.3,1.7,2.2,2.9,3.5,4.1,4.8,5.4,6,6.5,7.3,8,8.6,9,10]) 
plt.errorbar(x, y, xerr=0.1, yerr=0.1, c='black', lw=0.5, mfc='white', ms=3) 
ax.plot(-x,y,'ko', color = "midnightblue", markersize=4)  

# x=np.array([0,5.6,11.1,15,19.5,24.3,30.1,35.6,41.3,45,53,60,65.4,70.9,76.9,81.6,89.8,94.6,100,105.7,109.7,115.3,120]) 
# y=np.array([0,0.83,3,5.11,7.89,11.03,14.59,16.02,16.27,16.33,16.58,16.72,16.82,16.9,17,17.06,17.17,17.23,17.3,17.36,17.41,17.48,17.53]) 
# # plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='red', lw=0.5, mfc='white', ms=3) 

# ax.plot(x,y,'ko', color = "sandybrown", markersize=4) 
ax.legend(('$U_a=200 B$','$U_a=150 B$'))
plt.title('Зависимость анодного тока от напряжения на сетке')
plt.xlabel('$U_c$,В') 
plt.ylabel('$J_a$,мА') 
plt.grid () 
plt.xlim([-20,0]) 
plt.ylim([0,12]) 
plt.savefig('z01.png',dpi=300)
plt.show()
