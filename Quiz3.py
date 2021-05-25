# Quiz 3
# Harpreet kaur, Harman
import sys


class Account:
    def __init__(self, AccBalance):
        if AccBalance <= 0:
            print("Insufficient Balance in your Account")
        else:
            self.AccBalance = AccBalance

    def Credit(self, amount):
        self.AccBalance += amount

    def Debit(self, amount):

        if amount <= self.AccBalance:
            self.AccBalance -= amount

            return True
        else:
            print("Debit amount exceeded Account Balance..!! You have only: " + "'" + str(
                self.AccBalance) + "' " + " balance "
                                          "in your "
                                          "Account.")
            return False


class SavingsAccount(Account):
    def __init__(self, AccBalance, InterestRate):
        self.InterestRate = InterestRate
        super().__init__(AccBalance)

    def CalculateInterest(self):
        return self.AccBalance * self.InterestRate / 100


class CheckingAccount(Account):
    def __init__(self, balance, fee):
        self.fee = fee
        super().__init__(balance)

    def Credit(self, amount):
        super().Credit(amount)
        self.AccBalance -= self.fee

    def Debit(self, amount):
        if super().Debit(amount):
            self.AccBalance -= self.fee
            return True
        else:
            return False


print("Customer's Bank Accounts")

choice = ''
while choice != '0':
    choice = input(""""
        S.Simple Account
        SV.Saving Account.
        CA.Checking Account
        Q.Exit
        """"")
    if choice == 'S' or choice == 's':
        print("\n")
        # Main Account
        intBal = float(input("Enter the Initial Balance In Simple Account: "))
        acc = Account(intBal)
        print("The Initial Balance of Customer's Account is:   " + str(acc.AccBalance))
        crBal = float(input("Enter Amount that you want to added in your Simple Account: "))
        acc.Credit(crBal)
        print("Total Balance Of Simple Account after deposit: " + str(acc.AccBalance))
        drBal = float(input("Enter Amount that you Want to withdraw from Your Simple Account: "))
        acc.Debit(drBal)
        print("Total Balance of Simple Account after Withdraw: " + str(acc.AccBalance))

    elif choice == 'SV' or choice == 'sv':
        print("\n")
        intSavBal = float(input("Enter the Initial Balance In Saving Account: "))
        intRateSavBal = float(input("Enter Interest Rate that apply on Saving Account: "))
        chkSavingAcc = SavingsAccount(intSavBal, intRateSavBal)

        print("The Initial Balance of Customer's Saving Account is:   " + str(chkSavingAcc.AccBalance))

        print("The Interest Rate : " + str(intRateSavBal))
        print("\n")
        intRateBal = chkSavingAcc.CalculateInterest()
        print("The Amount of interest that earns by Saving Account : " + str(intRateBal))
        chkSavingAcc.Credit(intRateBal)
        print("The Total Balance of Saving Account(Initial Balance +Interest Amount): " + str(chkSavingAcc.AccBalance))
        print("\n")
        crSAvBal = float(input("Enter Amount that you want to added in your of Saving Account: "))
        chkSavingAcc.Credit(crSAvBal)
        print("Total Balance of your Saving  Account after deposit entry: " + str(chkSavingAcc.AccBalance))

        drSavBal = float(input("Enter Amount that you want to withdraw from your Saving Account: "))
        chkSavingAcc.Debit(drSavBal)
        print("Total Balance of your Saving  Account after withdraw Entry: " + str(chkSavingAcc.AccBalance))

        print("Final Updated Balance in Saving Account : " + str(chkSavingAcc.AccBalance))

    elif choice == 'CA' or choice == 'ca':
        # checking  account
        print("\n")
        intChkBal = float(input("Enter the Initial Balance In Checking Account: "))
        feeChkBal = float(input("Enter Fee Charge Per Transactions Checking Account: "))
        chkingAcc = CheckingAccount(intChkBal, feeChkBal)
        print("The Initial Balance of Customer's Checking Account is: " + str(chkingAcc.AccBalance))
        print("The Fee Charge per Transaction applied by Bank: " + str(feeChkBal))

        crChkBal = float(input("Enter Credit Amount that you want to add in your Checking Account: "))
        chkingAcc.Credit(crChkBal)

        print("Total Balance of Saving  Account after deposit entry(initial Balance-Transaction fee): " + str(
            chkingAcc.AccBalance))
        drChkBal = float(input("Enter Amount that you want to withdraw from your Checking Account: "))
        chkingAcc.Debit(drChkBal)
        print("Total Balance of Saving  Account after withdraw entry(initial Balance-Transaction fee): " + str(
            chkingAcc.AccBalance))

    elif choice == 'Q' or choice == 'q':
        sys.exit()
    else:
        print("Invalid choice ")
