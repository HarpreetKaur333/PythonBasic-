# Assignment 4
# Harpreet Kaur, Harman

# Question 1
from datetime import date

today = date.today()
currentDate = today.strftime("%d/%m/%Y")


class Rates:
    def __init__(self, firstName, lastName, yearOfBirth, currentYear):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__yearOfBirth = yearOfBirth
        self.__currentYear = currentYear

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def set_yearOfBirth(self, yearOfBirth):
        self.__yearOfBirth = yearOfBirth

    def set_currentYear(self, currentYear):
        self.__currentYear = currentYear

    def get_firstName(self):
        return self.__firstName

    def get_lastName(self):
        return self.__lastName

    def get_yearOfBirth(self):
        return self.__yearOfBirth

    def get_currentYear(self):
        return self.__currentYear

    def calculatesPersonAge(self):
        return self.__currentYear - self.__yearOfBirth

    def calculatesPersonMaximumHeartRate(self):
        return 220 - self.calculatesPersonAge()

    def calculatesPersonMaxMinTargetHeartRate(self):
        return self.calculatesPersonMaximumHeartRate() * 85 / 100, self.calculatesPersonMaximumHeartRate() * 50 / 100


class Profile:
    def __init__(self, firstName, lastName, gender, birthYear, birthMonth, birthDay, Weight, Height):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__gender = gender
        self.__birthYear = birthYear
        self.__birthMonth = birthMonth
        self.__birthDay = birthDay
        self.__Weight = Weight
        self.__Height = Height

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def set_gender(self, gender):
        self.__gender = gender

    def set_birthYear(self, birthYear):
        self.__birthYear = birthYear

    def set_birthMonth(self, birthMonth):
        self.__birthMonth = birthMonth

    def set_birthDay(self, birthDay):
        self.__birthDay = birthDay

    def set_Weight(self, Weight):
        self.__Weight = Weight

    def set_Height(self, Height):
        self.__Height = Height

    def get_firstName(self):
        return self.__firstName

    def get_lastName(self):
        return self.__lastName

    def get_gender(self):
        return self.__gender

    def get_birthYear(self):
        return self.__birthYear

    def get_birthMonth(self):
        return self.__birthMonth

    def get_birthDay(self):
        return self.__birthDay

    def get_Weight(self):
        return self.__Weight

    def get_Height(self):
        return self.__Height

    def calculatesPersonAge(self):
        todayDate = date.today()
        age = todayDate.year - self.__birthYear - (
                    (todayDate.month, todayDate.day) < (self.__birthMonth, self.__birthDay))
        return age

    def calculatesPersonMaximumHeartRate(self):
        return 220 - self.calculatesPersonAge()

    def calculatesPersonMaxMinTargetHeartRate(self):
        return self.calculatesPersonMaximumHeartRate() * 85 / 100, self.calculatesPersonMaximumHeartRate() * 50 / 100

    def calculatesIBM(self):
        return self.__Weight / self.__Height * self.__Height


def main():
    # Calling of Question 1 class methods
    print("Question 1")
    fName = str(input("Please User First Name: "))
    lName = str(input("Please User Last Name: "))
    yBirth = int(input("Please year of birth: "))
    cYear = int(input("Please  Current Year:  "))

    objRate = Rates(fName, lName, yBirth, cYear)

    ageY = objRate.calculatesPersonAge()
    mHR = objRate.calculatesPersonMaximumHeartRate()
    maxTR, minTR = objRate.calculatesPersonMaxMinTargetHeartRate()

    print(
        "Person First Name: " + "'" + str(objRate.get_firstName()) + "'" + "  Last Name: " + "'" + str(
            objRate.get_lastName()) + "'" + "  Year of "
                                            "Birth: "
        + "'" + str(objRate.get_yearOfBirth()) + "'")

    print("Person's age in years: " + str(ageY))
    print("Person's Maximum Heart Rate: " + str(mHR))
    print("Person's target-heart-rate range(Max to Min): " + str(maxTR) + " - " + str(minTR))
    print("\n")

    # Calling of Question 2 Class methods
    print("\n")
    print("\n")
    print("Question 2")
    print("\n")
    fName = str(input("Please User First Name: "))
    lName = str(input("Please User Last Name: "))
    gender = str(input("Please Gender: "))
    yBirth = int(input("Please year of birth: "))
    mBirth = int(input("Please month of birth: "))
    dBirth = int(input("Please day of birth: "))
    weight = int(input("Please  Weight of User: "))
    height = int(input("Please  height of User: "))

    objProfile = Profile(fName, lName, gender, yBirth, mBirth, dBirth, weight, height)

    ageInYear = objProfile.calculatesPersonAge()
    mHR1 = objProfile.calculatesPersonMaximumHeartRate()
    maxTR1, minTR1 = objProfile.calculatesPersonMaxMinTargetHeartRate()

    print(
        "Person First Name: " + "'" + str(objProfile.get_firstName()) + "'" + " Last Name: " + "'" + str(
            objProfile.get_lastName()) + "'" + " Gender: "
        + "'" + str(
            objProfile.get_gender())+"'" + " Date of Birth: " +"'"+str(objProfile.get_birthYear()) + "-" + str(
            objProfile.get_birthMonth()) + "-" + str(objProfile.get_birthDay())+"'" + " Weight: " +"'"+str(
            objProfile.get_Weight())+"'" + " Height: " + "'"+str(objProfile.get_Height())+"'")

    print("Person BMI: " + str(objProfile.calculatesIBM()))

    print("Person's age in years: " + str(ageInYear))
    print("Person's Maximum Heart Rate: " + str(mHR1))
    print("Person's target-heart-rate range(Max to Min).: " + str(maxTR1)+" - "+str(minTR1))


main()
