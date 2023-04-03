import math

n=input('Podaj liczbę n: ')
n=int(n)
if n<100 and n>0:
    for x in range(1,n+1):
        for b in range(1,n+1):
            print(x * b,end=' ')
        print('\n')
else:
    print('n is too large')