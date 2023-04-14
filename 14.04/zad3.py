class Romanian:
    def __init__(self,bilans):
        self.bilans = bilans
        self.slownik = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
    def dodawanie(self,ilosc):
        self.bilans += ilosc
    def odejmowanie(self,ilosc):
        if self.bilans - ilosc > 0:
            self.bilans -= ilosc
        else:
            return 'Odejmowanie nie zostalo wykonane'
    def mnozenie(self,ilosc):
        if ilosc > 0:
            self.bilans *= ilosc
        else:
            return 'Mnozenie nie zostalo wykonane'
    def len(self):
        pass
    def __str__(self):
        temp = self.bilans
        self.liczba = []
        if self.bilans==0:
            return "Liczba 0 nie istnieje w rzymskim zapisie"
        while self.bilans-1000>=0:
            self.liczba.append(self.slownik[1000])
            self.bilans-=1000
        while self.bilans - 500 >= 0:
            self.liczba.append(self.slownik[500])
            self.bilans -= 500
        while self.bilans-100>=0:
            self.liczba.append(self.slownik[100])
            self.bilans-=100
        while self.bilans-50>=0:
            self.liczba.append(self.slownik[50])
            self.bilans-=50
        while self.bilans-10>=0:
            self.liczba.append(self.slownik[10])
            self.bilans-=10
        while self.bilans-5>=0:
            self.liczba.append(self.slownik[5])
            self.bilans-=5
        while self.bilans-1>=0:
            self.liczba.append(self.slownik[1])
            self.bilans-=1
        self.bilans = temp
        return "Liczba rzymska od obecnej liczby "+str(self.bilans) +" to: " + str(self.liczba)

liczba = Romanian(100)
liczba2 = Romanian(50)
print(liczba)
print(liczba2)
liczba.odejmowanie(liczba2.bilans)
print(liczba)
liczba.mnozenie(10)
print(liczba)