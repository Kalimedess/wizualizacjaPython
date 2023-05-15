import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#zadania dla https://github.com/mwaskom/seaborn-data/blob/master/penguins.csv
data = pd.read_csv('jajka2023.csv', sep=",", encoding='Utf-8')
#punkt1
#print(data.groupby('sex')['body_mass_g'].mean())
#print(data.groupby('species')['body_mass_g'].mean())
#punkt2
#data2=data[data['body_mass_g']==data['body_mass_g'].min()]
#print(data2)
#data3=data[data['body_mass_g']==data['body_mass_g'].max()]
#print(data3)
#punkt3
#print(data.groupby('island').size().plot.bar())
#plt.show()
#ilość pingwinów każdego gatunku na każdej wyspie
#data2=data.groupby(['species','island']).size()
#print(data2)
#ilość pingwinów gatunku 'Adelie' na każdej wyspie
#print(data[data['species']=='Adelie'].groupby(['species','island']).size())
#colors=np.where(data['sex']=='MALE','blue','red')
#size=((data['body_mass_g']/450)**5/2000).copy()
#data.plot.scatter(x='bill_length_mm', y='bill_depth_mm', c=colors, s=size)
#plt.show()

#zadania dla https://github.com/mwaskom/seaborn-data/blob/master/tips.csv
