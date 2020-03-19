import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter 
fig = plt.figure() 
ax = fig.add_subplot(111) 

x=np.array([100,110,120,130,140,150,160,170,180,190,200,210,220]) 
y=np.array([0,0.1,0.1,0.15,0.3,0.4,0.6,1,1.4,1.9,2.5,3.2,4]) 
# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='blue', lw=0.5, mfc='white', ms=3) 
ax.plot(x,y,'ko', color = "orangered", markersize=4) 

x=np.array([90,100,110,120,130,140,150,160,166,170,176,180,186,192,200,206,210,216,220]) 
y=np.array([0,0.3,0.4,0.5,0.9,1.5,2,2.8,3.2,3.6,4.1,4.4,5,5.6,6.5,7.4,7.9,8.7,9.1]) 
# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='black', lw=0.5, mfc='white', ms=3) 
ax.plot(x,y,'ko', color = "midnightblue", markersize=4)  

# x=np.array([0,5.6,11.1,15,19.5,24.3,30.1,35.6,41.3,45,53,60,65.4,70.9,76.9,81.6,89.8,94.6,100,105.7,109.7,115.3,120]) 
# y=np.array([0,0.83,3,5.11,7.89,11.03,14.59,16.02,16.27,16.33,16.58,16.72,16.82,16.9,17,17.06,17.17,17.23,17.3,17.36,17.41,17.48,17.53]) 
# # plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='red', lw=0.5, mfc='white', ms=3) 

# ax.plot(x,y,'ko', color = "sandybrown", markersize=4) 
ax.legend(('$U_c=-8 B$','$U_c=-6 B$'))
plt.title('Зависимость анодного тока от напряжения на аноде')
plt.xlabel('$U_a$,В') 
plt.ylabel('$J_a$,мА') 
plt.grid () 
plt.xlim([80,225]) 
plt.ylim([0,12]) 
plt.savefig('z02.png',dpi=300)
plt.show()
