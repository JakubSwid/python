from sympy.abc import *
from sympy import *
import matplotlib.pyplot as plt


try:
    n=(int(input("Podaj ilość węzłów:")))
    if n<2:
        exit("To nie jest poprawna wartość!")
except:
    exit("To nie jest poprawna wartość!")
punkt_x=[]
punkt_y=[]

try:
    for i in range(n):
        punkt_x.append(float(input("Podaj punkt x" + str(i) + ":")))
        if punkt_x[-1] % 1 == 0:
            punkt_x[-1] = int(punkt_x[-1])
        punkt_y.append(float(input("Podaj punkt y" + str(i) + ":")))
        if punkt_y[-1] % 1 == 0:
            punkt_y[-1] = int(punkt_y[-1])
except:
    exit("To nie jest poprawna wartość!")
#print(punkt_x,punkt_y)

if len(punkt_x) > len(set(punkt_x)):
     exit("Elementy x muszą się różnić!")

f=1
g=0

for i in range(len(punkt_y)):
    for j in range(len(punkt_x)):
        if(i!=j):
            f*=(x-punkt_x[j])/(punkt_x[i]-punkt_x[j])
    f*=punkt_y[i]
    g+=f
    f=1



g=expand(g)
print(g)
print(" ")
pprint(g)

pr=(max(punkt_x)-min(punkt_x))*0.2
plot(g,(x,min(punkt_x)-pr,max(punkt_x)+pr),show=True)
plt.plot(punkt_x, punkt_y, 'o')
for i, j in zip(punkt_x, punkt_y):
     plt.annotate('(%s, %s)' % (i, j), xy=(i, j), textcoords='offset points', xytext=(0,10), ha='center')
plt.show()


