import numpy as np

Panstwo = np.array(['China','Japan','Germany','USA','South Korea','India','Brazil','Mexico','Spain','Russia'])
rok_1999 = np.array([0.56,8.1,5.3,5.63,2.36,0.53,1.1,0.99,2.28,0.94])
rok_2014 = np.array([19.91,8.27,5.6,4.25,4.12,3.15,2.31,1.91,1.89,1.69])

dziesietne=(rok_2014-rok_1999)/rok_1999
for x in range(len(Panstwo)):
    print(f'{Panstwo[x]} : {dziesietne[x]*100:.2f}%')


print(Panstwo[rok_1999>5])
