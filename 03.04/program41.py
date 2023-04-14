names = [ "michal" , "nela" , "ola" , "przemek" ]

names2 = [x.capitalize() for x in names]
print(names2)

names3 = [x for x in names if 'l' in x]
print(names3)

names4 = (x.capitalize() for x in names if 'a' in x[len(x)-1])
names5=[x for x in names4]
print(names5)


odp=0
for x in names:
     odp+=len(x)
print(odp)

def iloczyn(*numbers):
    odp=1
    for x in numbers:
        odp*=x
    return odp
print(iloczyn(1,3,45,6,7,3,54))

def sumaPoteg(*numbers, n):
    odp=0
    for x in numbers:
        odp+=x**n
    return odp
print(sumaPoteg(2,2,n=2))

def mean(*numbers):
    odp=0
    for x in numbers:
        odp+=x
    return odp/len(numbers)
def gmean(*numbers):
    odp=1
    for x in numbers:
        odp*=x
    return odp**(1/len(numbers))
print(mean(1,2,3,4,5,6))
print(gmean(2,4,8))

def sumaStr(*strings):
    odp=0
    for x in strings:
        odp+=len(strings)
    return odp

def checkTel(**phoneBook):
    for key, value in phoneBook.items():
        print(key,"ma numer",value)

phone_book = {'Anna':1234,'Bartosz':2345,'Cezar':5467}
checkTel(**phone_book)
phone_book2 = {'Adam':'12345435654','Bar':'24324345','Siz':'5467'}
checkTel(**phone_book2)

przychod = {'Styczen':123241,'Luty':234345235,'Marzec':21354634,'Kwiecien':24123412}
def wzrosty(**przychod):
    srAr=0
    srGeo=1
    for keys, values in przychod.items():
        srAr+=values
        srGeo*=values
    return srAr/len(przychod),srGeo**(1/len(przychod))

print(wzrosty(**przychod))

