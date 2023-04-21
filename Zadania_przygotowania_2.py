
def temperatury(n,k):
    if(k=='C'):
        print('Celsjusze = '+str(n)+'\nFahrenheity = '+str((n*(9/5)+32))+'\nKelwin = '+str((n+273.15)))
    elif(k=='F'):
        print('Celsjusze = ' + str((n-32)*(5/9)) + '\nFahrenheity = ' + str(n) + '\nKelwin = ' + str((n + 459.67)*(5/9)))
    elif(k=='K'):
        print('Celsjusze = ' + str((n-273.15)) + '\nFahrenheity = ' + str((n * (9 / 5) - 459.67)) + '\nKelwin = ' + str(n))

temperatury(10,'K')