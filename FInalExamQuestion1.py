# Final Exam Question 1 Harpreet Kaur(student id: 2031314)

class Auto:
    def __init__(self, Model, Cylinder):
        self.Model = Model
        self.Cylinder = Cylinder

    def getModel(self):
        return self.Model

    def getCylinder(self):
        return self.Cylinder

    def Engine(self):
        raise NotImplemented

    def Accelerate(self):
        raise NotImplemented

    def breakCar(self):
        raise NotImplemented


class Car(Auto):
    def __init__(self, Name, Model, Cylinder):
        self.Name = Name
        super().__init__(Model, Cylinder)

    def Engine(self):
        return self.Name + " Car Engine is starting "

    def Accelerate(self):
        return self.Name + " Accelerating the Car "

    def breakCar(self):
        return self.Name + " Break the Car "


def main():
    Car1 = Car("Tesla", "Model3", "electric-power")
    Car2 = Car("BMW", "BMW6", "Diesel ")
    Car3 = Car("Ford ", "Expedition Max", "Diesel")
    print(
        "Car Name: " + "'" + Car1.Name + "'" + " Model  " + "'" + Car1.Model + "'" + " using cylinder "
        + "'" + Car1.Cylinder + "'" + " , " + "'" + Car1.Engine() + "'" +
        " and going to accelerate to 100  " + "'" + Car1.Accelerate() + "'" + " and apply break on red light"
        + " '" + Car1.breakCar() + "'")
    print("\n")

    print(
        "Car Name: " + "'" + Car2.Name + "'" + " Model  " + "'" + Car2.Model + "'" + " using cylinder "
        + "'" + Car2.Cylinder + "'" + " , " + "'" + Car2.Engine() + "'" +
        " and going to accelerate to 100  " + "'" + Car2.Accelerate() + "'" + " and apply break on red light"
        + " '" + Car2.breakCar() + "'")
    print("\n")
    print(
        "Car Name: " + "'" + Car3.Name + "'" + " Model  " + "'" + Car3.Model + "'" + " using cylinder "
        + "'" + Car3.Cylinder + "'" + " , " + "'" + Car3.Engine() + "'" +
        " and going to accelerate to 100  " + "'" + Car3.Accelerate() + "'" + " and apply break on red light"
        + " '" + Car3.breakCar() + "'")
    print("\n")


# Call the main function.
main()
