import numpy as np
import pandas as pd

n=pd.Series([1,2,3,4,5])
strs=pd.Series(["Raz","Dwa","Trzy","Cztery"])
list=[1,2,3,4,5]
serlist=pd.Series(list)
lista2=[x for x in serlist]
tab = np.array([1,2,3,4])
serlist2=pd.Series(tab)
tab2 = np.array([x for x in serlist2])
tab3 = pd.Series(np.linspace(-10,10,201))
serlist3=pd.Series(x for x in tab3.sample(10,ignore_index=True) if x<0)
print(serlist3)
print("B")
my_list=[1,32,-37,91,12,11,-5]
my_dict={"a":[1,3,2],"b":[2,5,7],"c":[3,4,8],"d":[4,10,12]}
my_array=np.array([[1,2,5],[-2,3,3],[5,2,6]])
my_series=pd.Series([1,32,-37,91,12,11,-5],index=['a','b','c','d','e','f','g'])
dataFrame=pd.DataFrame({"lista":pd.Series((x for x in my_list),index=['a','b','c','d','e','f','g']),"slownik":pd.Series((x for x in my_dict.values()),index=['a','b','c','d']),"tablica":pd.Series((x for x in my_array),index=['a','b','c']),"seria":pd.Series((x for x in my_series),index=['a','b','c','d','e','f','g'])})
print(dataFrame)
my_list2=dataFrame["lista"].values.tolist()
print("Lista: ",my_list2)
my_dict2=dataFrame["slownik"].to_dict()
print("Slownik: ",my_dict2)
my_array2=dataFrame["tablica"].to_numpy()
print("Tablica",my_array2)
my_series2=dataFrame["seria"]
print("Seria:\n",my_series2)
print("C\n")
series=pd.DataFrame({"a":[1,-3,2],"b":[-3,8,0.5],"c":[2,-5,7],"d":[5,10,3]},index=['l1','l2','l3'])
print(series,'\n')
print(series.sort_values('a'),'\n')
print(series["a"]["l3"])
print(series.transpose(),'\n')
print(series.replace(10,1000))
