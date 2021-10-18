
class Parent:
    def __init__(self, m, n):
        self.fn = m
        self.sn = n
        print("in parent")

    def parentmethod(self):
        print ("parent method")


class Child(Parent):
    def __init__(self, m, n, j ,k):
        super().__init__(m,n)
        self.tn = j
        self.fon = k
        print("in child cons")

    def childmethod(self):
        print("child method", self.fn, self.sn, self.tn, self.fon)


c=Child(10,20, "python", "java")
c.childmethod()

