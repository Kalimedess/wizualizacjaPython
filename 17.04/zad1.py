def showList(tab):
    for x in tab:
        print(str(x))

lista = ['Apple','Banana','Monkey','Opel']
showList(lista)
print('\n')

stri = 'Adam Zapalka#@$@%#$'
def reverse(a):
    reversed_substring = ''
    for x in a[::-4]:
        if x.isalnum():
            reversed_substring += x
        else:
            pass
    return reversed_substring

print(reverse(stri))
print('\n')
def recur(n):
    if n==0 or n==1:
        return 1
    else:
        return recur(n-1)+recur(n-2)
def NonRecur(n):
    a = 0
    b = 1
    while n > 0:
        c = a + b
        a, b = b, c
        n = n - 1
    return c


print(recur(10))
print(NonRecur(10))

def nthPow(*licz,n=2):
    wyn=1
    for x in licz:
        wyn *= (x**n)
    return wyn
print(nthPow(1,2,3,4,5, n=2))
print('\n')
list = ['apple','banana','pomegranate','plum','orange','melon','cherry','watermelon']
newList = [a for a in list if 'o' in a or 'u' in a]
print(newList)
print('\n')

def Newton(n,k):
    factN = 1
    factK = 1
    factNK = 1
    if k==0 or k==n:
        return 1
    if k>n:
        return 0
    if n-1==k or k==1:
        return n
    for x in range(1,n+1):
        factN *= x
    for x in range(1,k+1):
        factK *= x
    for x in range(1,n-k+1):
        factNK *= x
    return factN/(factK*factNK)
print(Newton(7,2))
print('\n')
class Polynominal:
    def __init__(self,*wielomian):
        self.wielomian = []
        for x in reversed(wielomian):
            self.wielomian.append(x)

    def __add__(self, otherWielomian):
        if len(self.wielomian)>len(otherWielomian.wielomian):
            x = len(otherWielomian.wielomian)-1
            while x >= 0:
                self.wielomian[x] += otherWielomian.wielomian[x]
                x-=1
        else:
            x = len(self.wielomian) - 1
            while x >= 0:
                self.wielomian[x] += otherWielomian.wielomian[x]
                x -= 1
        return self.__str__()

    def __sub__(self, otherWielomian):
        if len(self.wielomian)>len(otherWielomian.wielomian):
            x = len(otherWielomian.wielomian)-1
            while x >= 0:
                self.wielomian[x] -= otherWielomian.wielomian[x]
                x-=1
        else:
            x = len(self.wielomian) - 1
            while x >= 0:
                self.wielomian[x] -= otherWielomian.wielomian[x]
                x -= 1
        return self.__str__()

    def __str__(self):
        x = len(self.wielomian)-1
        string = ''
        while x >= 0:
            if self.wielomian[x] > 0 and x != len(self.wielomian)-1:
                string += ' + '
            elif self.wielomian[x] < 0:
                string += '  '

            if x==0:
                string += str(self.wielomian[x])
            else:
                if self.wielomian[x]==0:
                    pass
                else:
                    string += str(self.wielomian[x]) + 'x^' + str(x)



            x-=1
        return string

wielomian = Polynominal(-2,3,4,6)
wielomian2 = Polynominal(3,2,3)
wielomian3 = Polynominal(2,3,3,4)
print(wielomian)
wielomian += wielomian2
print(wielomian)
wielomian3 -= wielomian2
print(wielomian3)