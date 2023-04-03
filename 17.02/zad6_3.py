import math

def euler(n):
    e1=(1+1/n)**n
    return e1
k=0
def elr2(n):
    e2=0
    for x in range(0,n):
        e2+=1/math.factorial(k)
    return e2

print(elr2(100))
print(euler(100)-math.e)
print(elr2(100)-math.e)
print(math.fabs(euler(100)-math.e))
print(math.fabs(elr2(100)-math.e))