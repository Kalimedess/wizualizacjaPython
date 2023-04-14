class Fruit:
    def __init__(self, color, weight):
        self.weight = weight
        self.color = color
    def isfresh(self,color):
        if self.color == 'brown':
            return False
        else:
            return True
    def __str__(self):
        return "color: "+str(self.color)+"\nweight: "+str(self.weight)
    def __add__(self,other):
        return "color: "+str(self.color)+"+"+str(other.color)+"\nweight: "+str(self.weight+other.weight)

class Apple(Fruit):
    pass
class Orange(Fruit):
    pass
class Banana(Fruit):
    pass

fruit1 = Apple('brown',2)
fruit2 = Orange('orange',3)
fruit3 = Banana('yellow',1)

print(fruit1)
print(fruit2)
print(fruit3)
print(fruit1+fruit2)

print(fruit1.isfresh(fruit1.color))
print(fruit2.isfresh(fruit2.color))
print(fruit3.isfresh(fruit3.color))