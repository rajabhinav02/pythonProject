from checking import test


class testchild(test):

    e=6

    def __init__(self,j,k):
        print("execute first")

        self.third = j
        self.fourth = k


        test.__init__(self,6,7)

    def testagain(self):
        return self.e+self.calcone()+self.fourth+self.third


testingagain= testchild(8,9)

print (testingagain.testagain())