class Account:
    def __init__(self,saldo):
        self.saldo = saldo

    def przelew_miedzy_kontami(self,otherAcc,ilosc,operacja):
        if operacja == 'wyplata':
            otherAcc.saldo -= ilosc
            self.saldo += ilosc
            return 'Otrzymano ' + str(ilosc) + " pieniedzy z drugiego konta, nowy bilans konta to: "+ str(self.saldo)
        elif operacja == 'wplata':
            if self.saldo - ilosc >= 0:
                otherAcc.saldo += ilosc
                self.saldo -= ilosc
                return 'Przelano '+str(ilosc)+" pieniedzy na drugie konto, nowy bilans konta to: "+ str(self.saldo)
            else:
                return 'Zbyt malo srodkow, przelew nie zostanie wykonany'
        else:
            return 'Przelew nie moze zostac wykonany, nieprawidlowa operacja'

    def wplata(self,moneyAdd):
        self.saldo += moneyAdd
        return 'Wplacono '+str(moneyAdd)+' na konto, nowy bilans konta to: '+ str(self.saldo)

    def wyplata(self,moneyRemove):
        if self.saldo - moneyRemove >= 0:
            self.saldo -= moneyRemove
            return 'Wyplacono ' + str(moneyRemove) + ' z konta, nowy bilans konta to: ' + str(self.saldo)
        else:
            return 'Zbyt malo srodkow, przelew nie zostanie wykonany'

    def przelew_zewnetrzny(self,ilosc,operacja):
        if operacja == 'wyplata':
            self.saldo += ilosc
            return 'Otrzymano ' + str(ilosc) + " pieniedzy z zewnetrznego konta, nowy bilans konta to: "+ str(self.saldo)
        elif operacja == 'wplata':
            if self.saldo - ilosc >= 0:
                self.saldo -= ilosc
                return 'Przelano '+str(ilosc)+" pieniedzy na zewnetrzne konto, nowy bilans konta to: "+ str(self.saldo)
            else:
                return 'Zbyt malo srodkow, przelew nie zostanie wykonany'
        else:
            return 'Przelew nie moze zostac wykonany, nieprawidlowa operacja'

    def __str__(self):
        return "Obecny bilans konta: " + str(self.saldo)

class PrivateAccount(Account):
    def __init__(self,saldo,wynagrodzenia):
        self.saldo = saldo
        self.wynagrodzenia = wynagrodzenia
    def __str__(self):
        return "Wynagrodzenia twoich pracownikow to: " + str(self.wynagrodzenia)

class FirmAccount(Account):
    def __init__(self,saldo,przelewyDoZus):
        self.saldo = saldo
        self.przelewyDoZus = przelewyDoZus
    def __str__(self):
        return "Twoje przelewy do Zus w ostatnim miesiacu to: "+ str(self.przelewyDoZus)


konto1 = Account(1000)
konto2 = Account(500)
konto3 = Account(600)
kontoPriv = PrivateAccount(100,{"mike pence":1000,"michael zapalka":100000})


print(kontoPriv.wplata(1000))
print(kontoPriv)
print(konto1.wplata(10000))
print(konto2.wyplata(100))
print(konto3.przelew_zewnetrzny(100000,'wplata'))
print(konto1.przelew_miedzy_kontami(konto2,200,'eawfsdaa'))
print(konto1.przelew_miedzy_kontami(konto2,200,'wyplata'))