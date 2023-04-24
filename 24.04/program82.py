import numpy as np

A=np.array([[1,1,2],[2,1,0],[4,1,2]]).reshape(3,3)
B=np.array([[2,5,7],[2,8,0],[4,3,1]]).reshape(3,3)
print(A+B)
print("\n")
print(A*B)
print(np.multiply(A,B))
print('transpose')
print(np.transpose(A))
print('\npower -1')
print(np.power(A,1/1))
print('A ** 5')
print(A**5)
print('A power 5')
print(np.power(A,5))
print('det B')
print(B)
print(np.linalg.det(B))
print('B power -3')
print(np.power(B,1/(3)))

print("\n")
print("C AND D TASKS")
C=np.array([1,2,4]).reshape(3,1)
D=np.array([2,5,7])
print(C*D)
print(D*C)
print(np.multiply(C,D))
print(C+D)
print('\n')
print("E AND F TASKS")
E=np.array([[1,5],[2,1]]).reshape(2,2)
F=np.array([[2,1],[2,8]]).reshape(2,2)
print(E/F)
print(E//F)
print(E%F)