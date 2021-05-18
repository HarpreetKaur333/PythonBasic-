# Quiz2 (classes, functions)
#  HarpreetKaur , Harman

# Calling Question 5 Function
class Auto:
    def __init__(self, model, cylinder):
        self.model = model
        self.cylinder = cylinder

    def getModel(self):
        return self.model

    def getCyl(self):
        return self.cylinder

    def engine(self):
        raise NotImplemented

    def accelerate(self):
        raise NotImplemented

    def breakcar(self):
        raise NotImplemented


class Car(Auto):
    def __init__(self, name, model, cylinder):
        self.name = name
        super().__init__(model, cylinder)

    def engine(self):
        return self.name + " Starting Engine "

    def accelerate(self):
        return self.name + " Accelerating Car  "

    def breakCar(self):
        return self.name + " Disk Break Pressed  "


# Calling Question 4 function
class Person:
    def __init__(self, name, height, mass):
        self.name = name
        self.height = height
        self.mass = mass

    def myFunc(self):
        return self.mass / (self.height * self.height)


def main():
    # calling of Question1
    MarkHeight = int(input("Please Mark's  Height: "))
    MarkMass = int(input("Please  Mark's  Mass: "))
    JohnHeight = int(input("Please John's   Height: "))
    JohnMass = int(input("Please  John's   Mass: "))
    checkMassHeight(MarkHeight, MarkMass, JohnHeight, JohnMass)
    print("\n")

    # calling of question2
    JohnTeamScored1 = int(input("Please John Team Scored in First Game: "))
    JohnTeamScored2 = int(input("Please John Team Scored in Second Game: "))
    JohnTeamScored3 = int(input("Please John Team Scored in Third Game: "))
    print("\n")
    MikeTeamScored1 = int(input("Please Mike Team Scored in First Game: "))
    MikeTeamScored2 = int(input("Please Mike Team Scored in Second Game: "))
    MikeTeamScored3 = int(input("Please Mike Team Scored in Third Game: "))
    print("\n")
    MaryTeamScored1 = int(input("Please Mary  Team Scored in First Game: "))
    MaryTeamScored2 = int(input("Please Mary  Team Scored in Second Game: "))
    MaryTeamScored3 = int(input("Please Mary  Team Scored in Third Game: "))
    checkAverageScored(JohnTeamScored1, JohnTeamScored2, JohnTeamScored3, MikeTeamScored1, MikeTeamScored2,
                       MikeTeamScored3, MaryTeamScored1, MaryTeamScored2, MaryTeamScored3)

    # Question 3 Function
    def checkTotalTipBill(BillList):
        TipList = []
        totalList = []
        for b in BillList:
            if b < 50:
                tipFirstAmount = b * 20 / 100
                TipList.append(tipFirstAmount)
                totalList.append(tipFirstAmount + b)

            elif 50 < b < 200:
                tipSecondAmount = b * 15 / 100
                TipList.append(tipSecondAmount)
                totalList.append(tipSecondAmount + b)
            else:
                tipThirdAmount = b * 10 / 100
                TipList.append(tipThirdAmount)
                totalList.append(tipThirdAmount + b)

        print("First tip:  " + str(TipList[0]))
        print("Second tip: " + str(TipList[1]))
        print("Third tip: " + str(TipList[2]))
        print("\n")
        print("Final paid Amounts at first Restaurant(Bill+Tip): " + str(totalList[0]))
        print("Final paid Amounts at Second Restaurant(Bill+Tip): " + str(totalList[1]))
        print("Final paid Amounts at Third Restaurant(Bill+Tip): " + str(totalList[2]))
        print("\n")
        print("Basic Amount at First Restaurant: " + str(BillList[0]))
        print("Basic Amount at Second Restaurant: " + str(BillList[1]))
        print("Basic Amount at Third Restaurant: " + str(BillList[2]))
        print("\n")

    # Calling of Question3
    BillList = []
    # TipList = []
    JohnBill1 = int(input("Please entered John First Restaurants Bill: "))
    JohnBill2 = int(input("Please entered John Second Restaurants Bill: "))
    JohnBill3 = int(input("Please entered John Third Restaurants Bill: "))
    BillList.append(JohnBill1)
    BillList.append(JohnBill2)
    BillList.append(JohnBill3)
    checkTotalTipBill(BillList)


# Question 1 Function
def checkMassHeight(MarkHeight, MarkMass, JohnHeight, JohnMass):
    BMIMark = 0
    BMIJohn = 0
    BMIMark = MarkMass / (MarkHeight * MarkHeight)
    BMIJohn = JohnMass / (JohnHeight * JohnHeight)
    check = BMIMark > BMIJohn
    if check:
        print("Is Mark's BMI higher than John's? " + str(check))
    else:
        print("Is Mark's BMI higher than John's? " + str(check))


# Question 2 function
def checkAverageScored(JohnTeamScored1, JohnTeamScored2, JohnTeamScored3, MikeTeamScored1, MikeTeamScored2,
                       MikeTeamScored3, MaryTeamScored1, MaryTeamScored2, MaryTeamScored3):
    AverageScoredJohnTeam = 0
    AverageScoredMikeTeam = 0
    AverageScoredMaryTeam = 0
    AverageScoredJohnTeam = (JohnTeamScored1 + JohnTeamScored2 + JohnTeamScored3 / 3)
    AverageScoredMikeTeam = (MikeTeamScored1 + MikeTeamScored2 + MikeTeamScored3 / 3)
    AverageScoredMaryTeam = (MaryTeamScored1 + MaryTeamScored2 + MaryTeamScored3 / 3)
    print("Average Scored of John team:" + str(AverageScoredJohnTeam))
    print("Average Scored of Mike team:" + str(AverageScoredMikeTeam))
    print("Average Scored of Mary team:" + str(AverageScoredMaryTeam))
    print("\n")
    if (AverageScoredJohnTeam > AverageScoredMikeTeam) and (AverageScoredJohnTeam > AverageScoredMaryTeam):
        print("John Team got highest average score in Game")
    elif (AverageScoredMikeTeam > AverageScoredJohnTeam) and (AverageScoredMikeTeam > AverageScoredMaryTeam):
        print("Mike Team got highest average score in Game")
    elif (AverageScoredMaryTeam > AverageScoredJohnTeam) and (AverageScoredMaryTeam > AverageScoredMikeTeam):
        print("Mary Team got highest average score in Game")
    else:
         print("draw Game")

# function 4
    UName1 = str(input("Please First User Name: "))
    MHeight = int(input("Please First User Height: "))
    MMass = int(input("Please  First User  Mass: "))
    print("\n")
    UName2 = str(input("Please Second User Name: "))
    JHeight = int(input("Please Second User  Height: "))
    JMass = int(input("Please  Second User  Mass: "))

    p1 = Person(UName1, MHeight, MMass)
    p2 = Person(UName2, JHeight, JMass)

    BMIM = p1.myFunc()
    BMIJ = p2.myFunc()

    if BMIM > BMIJ:
        print(
            "Hello My Name is: " + "'" + p1.name + "'" + "  and having BMI:" + "'" + str(
                BMIM) + "'" + " that is higher than: " + "'" + p2.name + "'")
    else:
        print("Hello My Name is: " + "'" + p2.name + "'" + " and having BMI:" + "'" + str(
            BMIJ) + "'" + " that is higher than " + "'" + p1.name + "'")
    print("\n")

    # Function 5
    p1 = Car("BMW", "VDI", "LPG ")
    p2 = Car("Range Rover", "R20", "Diesel ")
    p3 = Car("Swift ", "Desire ", " Petrol  ")
    print(
        "My  First car name is " + p1.name + " model  " + p1.model + " using " + p1.cylinder + "now i am starting my "
                                                                                               "care " + p1.engine() +
        " going to accelerate to 50  " + p1.accelerate() + " oh Red light " + p1.breakCar())
    print("\n")

    print(
        "My  Second car name is " + p2.name + " model  " + p2.model + " using " + p2.cylinder + "now i am starting my "
                                                                                                "care " + p2.engine() +
        " going to accelerate to 50  " + p2.accelerate() + " oh Red light " + p2.breakCar())
    print("\n")

    print(
        "My  Third  car name is " + p3.name + " model  " + p3.model + " using " + p3.cylinder + "now i am starting my "
                                                                                                "care " + p3.engine() +
        " going to accelerate to 50  " + p3.accelerate() + " oh Red light " + p3.breakCar())


# Call the main function.
main()
