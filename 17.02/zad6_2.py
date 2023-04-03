import math

a=int(input("Podaj A: "))
b=int(input("Podaj B: "))

temp=math.gcd(a,b)
p=a//temp
q=b//temp
c=math.gcd(int(p//q))
if c==0:
    print(a,"/",b," = ",p,"/",q)
else:
    p/=c
    q/=c
    print(a,"/",b," = ",p,"/",q)
