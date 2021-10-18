class Fruit:

    def __init__(self):
        print("this is parent call cons")

    def nutrition(self):
        print("this is parent nutrition")

    def fruit_shape(self):
        print("this is parent shape")

class Mango(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print("this is child cons")



    def nutrition(self):
        print("this is child nutrition")

    def color(self):
        print ("this is child color")

f= Fruit()
m = Mango()

m.nutrition()
m.color()
m.fruit_shape()
f.nutrition()
f.fruit_shape()
