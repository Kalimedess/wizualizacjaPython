
class Frac:
    def __init__(self, numerator, denominator):
        gcd = self.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __sub__(self, other):
        common_denominator = self.denominator * other.denominator
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        return Frac(numerator, common_denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Frac(numerator, denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return Frac.gcd(b, a % b)

#próba numer 2
class Frac2:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if isinstance(other, Frac):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Frac(new_numerator, new_denominator)
        else:
            raise TypeError("Can only add Frac to another Frac")

    def __pow__(self, power):
        if isinstance(power, int) and power >= 0:
            return Frac(self.numerator ** power, self.denominator ** power)
        else:
            raise TypeError("Power must be a non-negative integer")

    def __ge__(self, other):
        if isinstance(other, Frac):
            return self.numerator * other.denominator >= other.numerator * self.denominator
        else:
            raise TypeError("Can only compare Frac to another Frac")

print(Frac(2,10)**2)
print(Frac(2,10)>=Frac(1,5))