import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter 
import pandas as pd
import numpy as np
from scipy import interpolate

file = pd.read_excel('../rec/chem2.xlsx')
plt.figure(1)
y=file['I1_а1, мА']
y=y[~np.isnan(y)]
x=file['U_а1, В'] 
x=x[~np.isnan(x)]
plt.plot(x,y,'ko', color = "sandybrown",
        markersize=4,label="$U_{\\text{с}}=-8$, В")



y=file['I_а2, мА']
y=y[~np.isnan(y)]
x=file['U_а2, В'] 
x=x[~np.isnan(x)]
plt.plot(x,y,'ko', color = "darkslateblue", markersize=4,
        label="$U_{\\text{с}}=-6$, В")



plt.xlabel('$U_{\\text{а}}$, В') 
plt.ylabel('$J_{\\text{а}}$, мА') 
plt.legend()
plt.grid(which='major',linestyle='-') 
plt.grid(which='minor',linestyle=':') 
plt.minorticks_on()
plt.savefig('fig4.pdf',bbox_inches="tight")

plt.figure(2)
R = 2.5 # 2.5 кОм
Uin = file['U_вх3, В']
Uin=Uin[~np.isnan(Uin)]
Uin=Uin[0]

Uout=file['U_вых3, мВ']/1000
Uout=Uout[~np.isnan(Uout)]


x=file['U_а3, В'] 
x=x[~np.isnan(x)]



Ri = Uin/Uout*R
plt.plot(x,Ri,'ko', color = "darkslateblue",
        markersize=4,label="$U_{\\text{с}}=-8$, В")
plt.xlabel('$U_{\\text{а}}$, В') 
plt.ylabel('$R, \\text{кОм}$') 
plt.legend()
plt.grid(which='major',linestyle='-') 
plt.grid(which='minor',linestyle=':') 
plt.minorticks_on()
plt.savefig('fig5.pdf',bbox_inches="tight")



plt.figure(3)
R = 2.5 # 2.5 кОм
Uin = file['U_вх4, В']
Uin=Uin[~np.isnan(Uin)]
Uin=Uin[0]

Uout=file['U_вых4, мВ']/1000
Uout=Uout[~np.isnan(Uout)]

x=file['U_с4, В'] 
x=x[~np.isnan(x)]


Ri = Uin/Uout*R
plt.plot(x,Ri,'ko', color = "darkslateblue",
        markersize=4,label="$U_{\\text{а}}=220$, В")
plt.xlabel('$U_{\\text{с}}$, В') 
plt.ylabel('$R, \\text{кОм}$') 
plt.legend()
plt.grid(which='major',linestyle='-') 
plt.grid(which='minor',linestyle=':') 
plt.minorticks_on()
plt.savefig('fig6.pdf',bbox_inches="tight")



plt.figure(5)

file = pd.read_excel('../rec/chem1.xlsx')
R = 2.5 # 2.5 кОм
Uin = file['U_вх4, мВ']
Uin=Uin[~np.isnan(Uin)]
Uin=Uin[0]
Uout=file['U_вых4, мВ']
Uout=Uout[~np.isnan(Uout)]
x=file['U_а4, В'] 
x=x[~np.isnan(x)]
S = Uout/Uin/R


file = pd.read_excel('../rec/chem2.xlsx')
y=file['I1_а1, мА']
Uin = file['U_вх3, В']
Uin=Uin[~np.isnan(Uin)]
Uin=Uin[0]
Uout=file['U_вых3, мВ']/1000
Uout=Uout[~np.isnan(Uout)]
x=file['U_а3, В'] 
x=x[~np.isnan(x)]
Ri = Uin/Uout*R



mu = S * Ri
plt.plot(x,mu,'ko', color = "darkslateblue",
        markersize=4,label="$U_{\\text{с}}=-8$, В")
plt.xlabel('$U_{\\text{а}}$, В') 
plt.ylabel('$\mu$')
plt.legend()
plt.grid(which='major',linestyle='-') 
plt.grid(which='minor',linestyle=':') 
plt.minorticks_on()
plt.savefig('fig7.pdf',bbox_inches="tight")

plt.figure(6)
R = 2.5e3 # 2.5 кОм
file = pd.read_excel('../rec/chem1.xlsx')
Uin = file['U_вх3, мВ']
Uin=Uin[~np.isnan(Uin)]
Uin=Uin[0]
Uout=file['U_вых3, мВ']
Uout=Uout[~np.isnan(Uout)]
x=file['U_с3, В']
x=x[~np.isnan(x)]
S = Uout/Uin/R 
Sfunc = interpolate.interp1d(x,S)
# Sfunc = np.poly1d(Sfunc)
x0 = np.linspace(min(x),max(x),1000)
x1 = x
# plt.plot(x0,Sfunc(x0))


file = pd.read_excel('../rec/chem2.xlsx')
y=file['I1_а1, мА']
Uin = file['U_вх4, В']
Uin=Uin[~np.isnan(Uin)]
Uin=Uin[0]
Uout=file['U_вых4, мВ']/1000
Uout=Uout[~np.isnan(Uout)]
x=file['U_с4, В']
x=x[~np.isnan(x)]
Ri = Uin/Uout*R
Rifunc = interpolate.interp1d(x,Ri)
# Rifunc = np.poly1d(Rifunc)




mu = Sfunc(x1) * Rifunc(x1)

plt.plot(x1,mu,'ko', color = "darkslateblue",
        markersize=4,label="$U_{\\text{а}}=220$, В")
plt.xlabel('$U_{\\text{с}}$, в') 
plt.ylabel('$\mu$')
plt.legend()
plt.grid(which='major',linestyle='-') 
plt.grid(which='minor',linestyle=':') 
plt.minorticks_on()
plt.savefig('fig8.pdf',bbox_inches="tight")

