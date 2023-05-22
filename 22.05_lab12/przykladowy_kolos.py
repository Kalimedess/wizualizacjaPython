import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#zadanie 1
height=np.array([153,154,154,155,158,159,160,161,163,164,169])
shoesize=np.array([5,6,6,6,5,7,6,5,6,7,10])
print(shoesize.mean())
print(shoesize.max())
print(height[shoesize==shoesize.max()].mean())
print(height[shoesize==shoesize.max()].min())
print(shoesize.mean())
print(height.mean())
print(height[shoesize>=10].min())
print(height[shoesize>=10].max())


#zadanie 2
#plt.style.use('dark_background')
#x=np.linspace(-2,2,30)
#sns.set_palette("pastel")
#sns.scatterplot(x=x,y=x,linestyle='dotted',s=20)
#sns.scatterplot(x=x,y=x**2,linestyle='dotted',s=20)
#plt.show()