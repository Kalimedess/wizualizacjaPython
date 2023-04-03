import math

def modul(x,y):
    if isinstance(x,int) and isinstance(y,int):
        return x%y
    elif isinstance(x,float) or isinstance(y,float):
        return math.fmod(x,y)

def logarytm(a,n):
    for k in range(2,n+2):
        print(math.log(a,k),end="|")

def expo(a):
    print(math.exp(a))
    print(math.e**a)
    print(math.pow(math.e,a))

print("Ceil zaokragla w gore za kazdym razem: ",end=" ")
print(math.ceil(3.14))
print("Round zaokragla w gore w przypadku liczby n>=5: ",end=" ")
print(round(3.61))
print("Round zaokragla w dol w przypadku liczby n<5: ",end=" ")
print(round(3.14))
print("Floor zaokragla w dol za kazdym razem: ",end=" ")
print(math.floor(3.14))
print("\n","Podpunkt 2")
print(math.remainder(5,3))
print(5%3)
print(modul(3,2))
print("\n","Podpunkt 3")
logarytm(16,10)
print("\n","Podpunkt 4")
expo(3)
