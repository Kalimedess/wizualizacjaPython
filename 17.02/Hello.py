def hello_world():
    print('Hello World!')

def kalkulator(a,b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a**b)
    if b == 0:
        print('Nie można dzielić przez 0!')
    else:
        print(a / b)

c=2
d=1
e=3
f=5
print(e-f)
print(e/f)
print('Wyniki z funkcji')
kalkulator(c,d)
hello_world()