
def parzyste(a):
    return a[::2]

def ostatnieZn(a,n=1):
    return a[len(a)-n::]

def odwrStr(a):
    return a[::-1]

def ktoryDluzszy(a,b):
    if len(a)>len(b):
        return a
    elif len(a)<len(b):
        return b
    else:
        return "Stringi sa tej samej dlugosci"

def wstawianieStr(a,b):
    odp="My name is {imie}. My date of birth is {dataUr}."
    odp=odp.format(imie=a,dataUr=b)
    return odp

print(parzyste("Lorem Ipsum"))
print(ostatnieZn("Lorem Ipsum",3))
print(odwrStr("Odwrocone"))
print(ktoryDluzszy("sit","site"))
print(wstawianieStr("Cezary","22-02-2002"))