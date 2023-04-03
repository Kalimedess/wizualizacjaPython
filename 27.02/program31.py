import math


list = []
for x in range(0,14):
    list.append(math.pow(x,5))

list2 = []
for x in range(0,19):
    list2.append(math.factorial(x))

list3 = []
for x in range(0,19):
    list3.append(pow(math.e,x))

list4 = ["Adamowski","Zapalka","Choracki"]
list5 = [len(x) for x in list4]


print("Podpunkt 1")
print(list)
print("Podpunkt 2")
print(list2)
print("Podpunkt 3")
print(list3)
print("Podpunkt 4")
print(list5)