class Rectangle():

    def __init__(self,l,w):
        self.length=l
        self.width=w

    def area(self):
        return self.length * self.width


rect = Rectangle(10,20)

print("The area is ",rect.area())