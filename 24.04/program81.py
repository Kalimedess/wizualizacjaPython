import numpy as np


my_array = np.arange(10,40,2)
print(my_array)
my_array+=3
print(my_array)
my_array*=2
print(my_array)
my_array[my_array%6==2]=0
print(my_array)

def change(A,x):
    B=A.copy()
    B[B==0]=x
    return B
arr=change(my_array,1)
print(arr)
