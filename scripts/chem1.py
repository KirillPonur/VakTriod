import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter 
import pandas as pd
import numpy as np
file = pd.read_excel('../rec/chem1.xlsx')

plt.figure(1)
y=file['I_а1, мА']
y=y[~np.isnan(y)]
x=file['U_с1, В'] 
x=x[~np.isnan(x)]
plt.plot(x,y,'ko', color = "sandybrown",
        markersize=4,label="$U_{\\text{а}}=220$, В")



y=file['I_а2, мА']
y=y[~np.isnan(y)]
x=file['U_с2, В'] 
x=x[~np.isnan(x)]
plt.plot(x,y,'ko', color = "darkslateblue", markersize=4,
        label="$U_{\\text{а}}=150$, В")



plt.xlabel('$U_{\\text{с}}$, В') 
plt.ylabel('$J_{\\text{а}}$, мА') 
plt.legend()
plt.grid(which='major',linestyle='-') 
plt.grid(which='minor',linestyle=':') 
plt.minorticks_on()
plt.savefig('fig1.pdf',bbox_inches="tight")






plt.figure(2)
R = 2.5e3 # 2.5 кОм
Uin = file['U_вх3, мВ']
Uin=Uin[~np.isnan(Uin)]
Uin=Uin[0]

Uout=file['U_вых3, мВ']
Uout=Uout[~np.isnan(Uout)]

x=file['U_с3, В'] 
x=x[~np.isnan(x)]


S = Uout/Uin/R
plt.plot(x,S,'ko', color = "darkslateblue",
        markersize=4,label="$U_{\\text{а}}=220$, В")

plt.xlabel('$U_{\\text{с}}$, В') 
plt.ylabel('$S, \\text{Ом}^{-1}$') 
plt.legend()
plt.grid(which='major',linestyle='-') 
plt.grid(which='minor',linestyle=':') 
plt.minorticks_on()
plt.savefig('fig2.pdf',bbox_inches="tight")


plt.figure(3)
Uin = file['U_вх4, мВ']
Uin=Uin[~np.isnan(Uin)]
Uin=Uin[0]
# print(Uin)

Uout=file['U_вых4, мВ']
Uout=Uout[~np.isnan(Uout)]
# print(Uout)

x=file['U_а4, В'] 
x=x[~np.isnan(x)]
print(x)


S = Uout/Uin/R
plt.plot(x,S,'ko', color = "darkslateblue",
        markersize=4,label="$U_{\\text{с}}=-8$, В")
plt.xlabel('$U_{\\text{а}}$, В') 
plt.ylabel('$S, \\text{Ом}^{-1}$') 
plt.legend()
plt.grid(which='major',linestyle='-') 
plt.grid(which='minor',linestyle=':') 
plt.minorticks_on()
plt.savefig('fig3.pdf',bbox_inches="tight")
plt.show()

