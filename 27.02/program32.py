import math

def numerMies(a):
    if(a=="Styczen"):
        return 0
    elif(a=="Luty"):
        return 1
    elif (a == "Marzec"):
        return 2
    elif (a == "Kwiecien"):
        return 3
    elif (a == "Maj"):
        return 4
    elif (a == "Czerwiec"):
        return 5
    elif (a == "Lipiec"):
        return 6
    elif (a == "Wrzesien"):
        return 7
    elif (a == "Sierpien"):
        return 8
    elif (a == "Pazdziernik"):
        return 9
    elif (a == "Listopad"):
        return 10
    elif (a == "Grudzien"):
        return 11

def pozniejNizPodana(a,b):
     odp=[]
     for x in a:
         if x[0] > b:
            odp.append(x)
     return odp

def wiekszaNiz6(a):
    odp=[x for x in a if len(x)>6]
    return odp

def czyPalindrom(a):
    temp1 = []
    temp2 = []
    for x in range(0,len(a)):
        temp1.append(a[x])
        temp2.append(a[x])
    temp2.reverse()
    if temp1==temp2:
        return True
    else:
        return False

def czyOdNajwiDoNajmn(a):
    temp=[x for x in a]
    temp.sort(reverse=True)
    if a==temp:
        return True
    else:
        return False

def potegaDo3(a):
    odp=[math.pow(x,3) for x in a]
    return odp

def func(list,n1,n2):
    return [x if x != n1 else n2 for x in list]

def func1(list,n1,n2,rel_tol=1e-09,abs_tol=0):
    return [x if (math.isclose(x,n1,rel_tol=rel_tol,abs_tol=abs_tol)==0) else n2 for x in list]

phone_book = {'Anna':1234,'Bartosz':2345}

def print_phone(book):
    for x in book.keys():
        print(x,":",book[x])

print_phone(phone_book)

def fun_palindrom(w):
    w = w.replace(" ","").lower()
    return w==w[-1::-1]

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [10,20,30,40,50,60,70,80,90,100]
list3 = []
print(list1+list2)
for x in range(0,len(list2)):
    list3.append(list1[x]+list2[x])
print(list3)
print("Podpunkt 2")
list4=["Czerwiec","Styczen","Luty"]
list4.sort(key=numerMies)
print(list4)
print("Podpunkt 3")
nazwiska=["Badamowski","Zapalka","Marcinowicz","Gora"]
print(pozniejNizPodana(nazwiska,'A'))
print("Podpunkt 4")
print(wiekszaNiz6(nazwiska))
print("Podpunkt 5")
print(czyPalindrom("ala"))
print(czyPalindrom("adam"))
print("Podpunkt 6")
list5=[1,2,3,4,5]
list6=[5,4,3,2,1]
print(czyOdNajwiDoNajmn(list6))
print(czyOdNajwiDoNajmn(list5))
print("Podpunkt 7")
list7=[1,2,3,4]
list8=[5,6,7,8]
print(potegaDo3(list7))
print(potegaDo3(list8))
