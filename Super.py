#Python example to show that base class members can be accessed in derived class using super() 

class Base(object):

    def __init__(self,x):

        self.x =x

class Derived(Base):

    def __init__(self,x,y):

        super().__init__(x)
        self.y=y

    def printvar(self):

        print(self.x,self.y)
       # print(Base.x,self.y) this wouldn't work as in the derived class we are using super not Base.x=x

derived = Derived(40,5)
derived.printvar()




