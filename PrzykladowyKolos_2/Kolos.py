import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
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
unique_heights = np.unique(height)
mean_shoe_sizes = []
cumulative_sum = 0
count = 0
for h in unique_heights:
    indices = np.where(height == h)
    shoe_sizes = shoesize[indices]
    cumulative_sum += np.sum(shoe_sizes)
    count += len(shoe_sizes)
    mean_shoe_size = cumulative_sum / count
    mean_shoe_sizes.append(mean_shoe_size)
    print(mean_shoe_size)

mean_shoe_sizes = np.array(mean_shoe_sizes)
print("Wzrost:", unique_heights, "cm | Średni rozmiar buta:", mean_shoe_sizes)

height=np.array([153,154,154,155,158,159,160,161,163,164,169])
shoesize=np.array([5,6,6,6,5,7,6,5,6,7,10])
print(shoesize.mean())
print(height[shoesize==shoesize.max()].mean())
height2=np.array(np.unique(height))
'''
#zadanie 2
'''
plt.style.use('dark_background')
x=np.linspace(-2,2,30)
sns.set_palette("pastel")
sns.scatterplot(x=x,y=x,linestyle='dotted',s=20)
sns.scatterplot(x=x,y=x**2,linestyle='dotted',s=20)
plt.show()
'''
#zadanie 3
#suma dla kazdego kandydata
kandydaci=["Robert BIEDROŃ","Krzysztof BOSAK","Andrzej Sebastian DUDA","Szymon Franciszek HOŁOWNIA",
           "Marek JAKUBIAK","Władysław Marcin KOSINIAK-KAMYSZ","Mirosław Mariusz PIOTROWSKI","Paweł Jan TANAJNO",
           "Rafał Kazimierz TRZASKOWSKI","Waldemar Włodzimierz WITKOWSKI","Stanisław Józef ŻÓŁTEK"]
data2=pd.read_csv('kandydaci_prez.csv',sep=';')
data3=data2.groupby("Kod TERYT")[kandydaci].sum()
print(data3.sum())

#podpunkt 4
kandydaci=["Robert BIEDROŃ","Krzysztof BOSAK","Andrzej Sebastian DUDA","Szymon Franciszek HOŁOWNIA",
           "Marek JAKUBIAK","Władysław Marcin KOSINIAK-KAMYSZ","Mirosław Mariusz PIOTROWSKI","Paweł Jan TANAJNO",
           "Rafał Kazimierz TRZASKOWSKI","Waldemar Włodzimierz WITKOWSKI","Stanisław Józef ŻÓŁTEK"]
data2=pd.read_csv('kandydaci_prez.csv',sep=';')
data3=data2.groupby("Kod TERYT")[kandydaci].sum()
data3.plot(kind='bar',stacked=True)
plt.legend(loc="upper right")
plt.show()

#podpunkt 3 sposobem jarka
dane=pd.read_csv("kandydaci_prez.csv",sep=';',index_col=1)
x=dane["Komisje obwodowe otrzymały kart do głosowania"].sum()
dane2=(dane["Liczba kopert zwrotnych, w których nie było oświadczenia o osobistym i tajnym oddaniu głosu"]/
       dane["Komisje obwodowe otrzymały kart do głosowania"])*100
dane2.plot(kind='bar')
plt.xticks(rotation=30)
kandydaci=["Robert BIEDROŃ","Krzysztof BOSAK","Andrzej Sebastian DUDA","Szymon Franciszek HOŁOWNIA",
           "Marek JAKUBIAK","Władysław Marcin KOSINIAK-KAMYSZ","Mirosław Mariusz PIOTROWSKI","Paweł Jan TANAJNO",
           "Rafał Kazimierz TRZASKOWSKI","Waldemar Włodzimierz WITKOWSKI","Stanisław Józef ŻÓŁTEK"]
for x in kandydaci:
    print(x)
    print(dane[x].sum())

dane3=dane.groupby(dane["Kod TERYT"])[kandydaci].sum()
dane3.plot(kind="bar",stacked=True)
plt.legend(loc='upper right')
plt.show()