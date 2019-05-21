class Base(object):

    def __init__(self,x):

        self.x=x

class Derived(object):

    def __init__(self,x,y):

        Base.x=x
        self.y=y

    def printvar(self):

        print(Base.x,self.y)

derived = Derived(10,20)
derived.printvar()

