class Base1(object):

    def __init__(self):
        self.str1 = "Hello"
        print("base1")

class Base2(object):

    def __init__(self):

        self.str2 = "Soumya"
        print("base2")

class Derived(Base1, Base2):

    def __init__(self):

        Base1.__init__(self)
        Base2.__init__(self)
        print("In derived class")
    
    def printStr(self):

        print(self.str1,self.str2)

derived = Derived()
derived.printStr()