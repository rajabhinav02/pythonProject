

class calc:
    num = 200
    #fn

    def test(self):
        print("testing")
        print (calc.num)


    def __init__(self, c, d):
        print("cons")
        self.tn = c
        self.en = d

    def testingagain(self):
        print("i am also being called")

    def calcy(self):
        print(self.tn)
        return self.tn+self.en+calc.num


#ob=calc(6,8)

#print(ob.num)
#ob.test()
#print(ob.calcy())
#ob.testingagain()

