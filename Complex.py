class ComplexNo():

    #default constructor with default values of imag and real as 0
    def __init__(self,r=0,i=0):
        self.real=r
        self.imag=i
    
    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

c1=ComplexNo(10,20)

c1.getData()
#c1.attr=30

c2=ComplexNo(40)
c2.getData()
#c2.attr = 10

#print(c2.getData,c2.attr)

