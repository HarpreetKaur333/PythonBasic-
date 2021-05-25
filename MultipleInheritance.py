class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    pass
    # def m(self):
    #     print("In Class2")


class Class3(Class1):
    pass
    # def m(self):
    #     print("In Class3")


class Class5(Class1):
    pass


class Class6(Class1):
    pass


class Class4(Class2, Class3, Class5, Class6):
    pass


obj4 = Class4()
obj4.m()


class ClassA:
    def m(self):
        print("In ClassA")


class ClassB(ClassA):
    def m(self):
        print("In ClassB")
        super().m()


class ClassC(ClassA):
    def m(self):
        print("In ClassC")
        super().m()


class ClassD(ClassB, ClassC):
    def m(self):
        print("In Class4")
        super().m()


ClassD.mro()
