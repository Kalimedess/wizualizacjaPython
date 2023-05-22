import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#x=np.linspace(-10,10,100)
#print(x)
#y=1/(1+x**2)
#plt.plot(x,y,'green',label='1/(1+x^2)')
#plt.legend(title='Wykres')
#plt.show()

#podpunkt2
#x=np.linspace(0,3,100)
#print(x)
#y=x**2
#y1=np.exp(x)
#y2=x**x
#plt.plot(x,y,'green',label='x^2')
#plt.plot(x,y1,'red',label='e^x')
#plt.plot(x,y2,'blue',label='x^x')
#plt.legend(title='Wykres')
#plt.show()

#podpunkt3
#x=np.linspace(0,4,100)
#fig,ax=plt.subplots(3)
#y=x**2
#y1=np.exp(x)
#y2=x**x
#ax[0].plot(x,y,'green',linestyle='--',label='x^2')
#ax[1].plot(x,y1,'red',linestyle=':',label='e^x')
#ax[2].plot(x,y2,'blue',label='x^x')
#fig.legend(title='Wykres',loc='upper center')
#plt.show()

#analiza kodu

#def sinplot (flip=1):
#    x = np.linspace(0,14,100)
#    for i in range(1,5) :
#        plt.plot(x,np.sin( x + i * .5) * (7-i) * flip)
#sns.set_style("whitegrid")
#sns.set_palette("husl")
#sinplot()
#print(sns.axes_style())
#plt.show()

#zadanie 3
xsqrt=np.linspace(0,2,100)
x=np.linspace(-2,2,100)
ysqrt=np.sqrt(xsqrt)
ysqrt1=np.power(xsqrt,(1/3))

sns.set_style("darkgrid")
sns.set_palette('dark')

plt.plot(xsqrt,ysqrt,'red')
plt.plot(xsqrt,ysqrt1,'purple')
for i in range(1,4):
    plt.plot(x,x**i)
plt.show()