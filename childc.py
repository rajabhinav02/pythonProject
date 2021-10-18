from classd import calc


class childclass(calc): #parent method is calc

    num2 = 300

    def __init__(self,c,d):
        


        calc.__init__(self, c,d) # calling parent constructor
        self.tn = c
        self.en = d

    def childme(self):
        print("inside child method")
        return self.num2+self.num+self.calcy()+self.tn+self.en



obj3 = childclass(10,20)
obj3.test()
print(obj3.calcy())

#obj3.testingagain()
print (obj3.childme())

