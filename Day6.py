#python interface
#go to env to find your python Scripts installation.in my case it is in:
#C:\Users\User\env\Scripts
#C:\>cd "C:\Users\User\env\Scripts"
#check your pip installation: pip --version
#if by any chance you dont have pip, in order to install it chec: liquidweb.com/kb/install-pip-windows
#pip install python-interface
#another way: just click on the red lined implements,Interface header

from interface import implements, Interface
class MyInterface(Interface):
    def method1(self,x):
        pass
    def method2(self,x,y):
        pass

class MyClass(implements(MyInterface)):
    def method1(self,x):
        return x*2
    def method2(self,x,y):
        return x+y

myInstance = MyClass()
print(myInstance.method1(4))
print(myInstance.method2(4,5))




#creating an interface by making (hard coding) all methods abstracts
class Shape:
    def __init__(self):
        if type(self) is Shape:
            raise NotImplementedError('absract class can not be instantiated')

    def draw(self):
        pass
#
#
class Circle(Shape):
    def __init__(self):
        super().__init__()

    def draw(self):
        print("inside Circle::draw() method")

class Square(Shape):

    def draw(self):
        print("inside Square::draw() method")

class Rectangle(Shape):

    def draw(self):
        print("inside Rectangle::draw() method")


class ShapeFactory:
    @staticmethod
    def getshape(shapetype):
        if shapetype == "CIRCLE":
            return Circle()
        elif shapetype == "RECTANGLE":
            return Rectangle()
        elif shapetype == "SQUARE":
            return Square()
        else:
            return None

class MyShapes:

    def main(self):
        c = ShapeFactory.getshape("CIRCLE")
        c.draw()
        r = ShapeFactory.getshape("RECTANGLE")
        r.draw()
        s = ShapeFactory.getshape("SQUARE")
        s.draw()

m= MyShapes()
m.main()




# #using the interface package
from interface import implements, Interface
class Shape(Interface):
    def draw(self):
        pass

class Circle(implements(Shape)):

    def draw(self):
        print("inside Circle::draw() method")

class Square(implements(Shape)):

    def draw(self):
        print("inside Square::draw() method")

class Rectangle(implements(Shape)):

    def draw(self):
        print("inside Rectangle::draw() method")


class ShapeFactory:

    def getshape(self,shapetype):
        if shapetype == "CIRCLE":
            return Circle()
        elif shapetype == "RECTANGLE":
            return Rectangle()
        elif shapetype == "SQUARE":
            return Square()
        else:
            return None

class MyShapes:

    def main(self):
        myshape = ShapeFactory()
        c = myshape.getshape("CIRCLE")
        c.draw()
        r = myshape.getshape("RECTANGLE")
        r.draw()
        s = myshape.getshape("SQUARE")
        s.draw()

m= MyShapes()
m.main()



##a longer example of classes.
#absract class Animal
class Animal:
    def __init__(currentobject,age,gender,weight):
        raise NotImplementedError("abstract class cannot be instantiated")

    def sleep(currentobject):
        print("the animal is sleeping")

    def eat(currentobject):
        print("the animal is eating")

    def speak(currentobject):
        print("the animal age is " + str(currentobject.age) + " years old")
        print("the animal weight is " + str(currentobject.weight) + " kg")
        print("the animal gender is " + currentobject.gender)

    def move(currentobject):
        raise NotImplementedError("hey, put some code here")

class Bird(Animal):
    def __init__(self,age,gender,weight):
        self.age=age
        self.gender = gender
        self.weight = weight

    def move(self):
        print("the bird is flying")


#lets test this
# x = Bird(2,"female",6)
# x.speak()

class Chicken(Bird):
    def move(self):
        print("the chick is clapping wings")

#lets test this
# y=Chicken(3,"female",10)
# y.move()

from interface import implements,Interface
class Singable(Interface):
    def sing(self):
        pass

class Sparrow(Bird,implements(Singable)):
    def move(self):
        print("Sparrow flying high")
    def sing(self):
        print("the sparrow is singing like Celine Dion")

#lets test it
# s = Sparrow(4,"male",5)
# s.sing()

class Perrokee(Bird,implements(Singable)):
    def move(currentobject):
        print("the perrokee is flying from one tree to another one")
    def sing(self):
        print("the Perrokee is singing like Deepika pudokone")

# p=Perrokee(7,"female",3)
# p.move()
# p.sing()

class Kangaroo(Animal):
    def __init__(self,age,gender,weight):
        self.age = age
        self.gender=gender
        self.weight=weight
    def move(self):
        print("the kangaroo is jumping...")

class Fish(Animal):
    def __init__(self,age,gender,weight):
        self.age = age
        self.gender=gender
        self.weight=weight
    def move(self):
        print("the fish is swimming...")

class Zoo:
    def main(self):
        b=Bird(1,"female",10)
        b.move()
        c=Chicken(2,"female",20)
        c.move()
        s=Sparrow(3,"male",30)
        s.move()
        print("moveanimal dynamic")
        z = Zoo()
        z.moveanimal(b)
        z.moveanimal(c)
        z.moveanimal(s)

    def moveanimal(self,animal):
        animal.move()

    @staticmethod
    def moveAnimal(animal):
        animal.move()



m = Zoo()
m.main()
print("this one is static moveAnimal")
mySparrow = Sparrow(10,"male",100)
Zoo.moveAnimal(mySparrow)