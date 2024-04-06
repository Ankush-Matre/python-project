class BalanceException(Exception):
    pass

class BankAccount():
    #here we create a class name is Bankaccount 
    def __init__(self , AccountBalance , AccountName ):
        #THis is a init function of the python which we declare the two
        #variable account balance and the accountName
        #it is nothing but the parameterise constructor which is automatically 
        #called when the object of the class is created

        self.balance = AccountBalance
        self.name = AccountName
        print(f"\nAccount {self.name } Created. ")
        print(f"\nBalance is ${self.balance: .2f} ")

    def showbalance(self):
        print(f"\nAccount balance of the '{self.name }' is == ${self.balance: .2f} ")
    #this function is used to show the money in the bank
    def deposite(self, amount ):
        #money = input("\nDo you want to deposite money in the bank ? : ")
        #if(money == 'yes'):
        self.balance = self.balance + amount
        print("\nDEPOSITE IS COMPLETE 👍👍!!")
        self.showbalance()
    
    def Transaction(self , amount):
        #This function is use to do transaction and it checks whether the amount 
        # is less or greater than the balance
        if(self.balance >= amount ):
            return
        else:
            raise BalanceException(f"Sorry '{self.name}' You only has balance ${self.balance : .2f}")
    
    def Withdraw(self , amount):
        try:
            #in the try section we can add
            self.Transaction(amount)
            self.balance = self.balance - amount
            print("\n Withdraw is Completed 👍👍 !!")
            #self.showbalance()
        except BalanceException as error :
            print(f"\nWithdrawal intrrupted {error} !!!!! ")
    
    def transfer(self, amount ,account):
        try:
            print("\n********* Beginning the Transfer....🚀 **********")
            self.Transaction(amount) 
            self.Withdraw(amount)
            #account.deposite(amount)
            print("\nTransfer Completed !! 👍👍👍 ")
        except BalanceException as error :
            print(f"Transfer Intrrupted ❌❌. {error} ")

class interestsrewardacct(BankAccount):
    # here we inherit the above class from the BankAccount class
    def deposite(self, amount):
        #deposite method is overide with class Bankaccount with deposite method
        #here we give the 5% interest 
        self.balance = self.balance + ((amount * 5) / 100 ) + amount
        print("\nDEPOSITE IS COMPLETE 👍👍!!")
        #self.showbalance()

class sevingsAccount(interestsrewardacct):
    #This class is inherited from the intrestsrewardsacct class
    # here we charge some fee for that perpose we can use this class

    def __init__(self, intialAmount , acctName):
        super().__init__(intialAmount , acctName)
        #here the super keyword is used to access the method the method of the
        # parent class by which we call the methods of the parent class\
        self.fee = 5

    def Withdraw(self, amount):
        try:
            self.Transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw is Completed 👍👍 !!")
            self.showbalance()
        except BalanceException as error:
            print(f"Transfer Intrrupted ❌❌. {error} ")



if (__name__ == '__main__'):
    a = BankAccount(1000 , 'ANKUSH')
    s = sevingsAccount(2000 , 'MATRE')
    print("***** WELCOME TO THE ANKUSH BANK *****")

    while(True):
        print("Enter the Choices To continue with the BANK ")
        print("1.Show Your Balance")
        print("2.Deposite Money in the bank")
        print("3.Withdraw Your money")
        print("4.Transfer your Amount")
        choice = input()
        if choice not in ['1' , '2' ,'3', '4' ]:
            print("Enter the Valid Option")
            continue
        else:
            choice = int(choice)

        if(choice == 1):
            #a.showbalance()
            s.showbalance()

        elif(choice == 2):
            amount = int(input("Enter the Amount You have to Deposite : "))
            #a.deposite(amount)
            s.deposite(amount)


        elif(choice == 3):
            amount = int(input("Enter the amount of that You Withdraw : "))
            #a.Withdraw(amount)
            s.Withdraw(amount)
        
        elif(choice == 4):
            amount = int(input("Enter the amount of that You Transfer : "))
            account = input("Enter the name of account that You want to trasfer the amount : ")
            #a.transfer(amount , account)
            s.transfer(amount , account)




        

a = BankAccount(1000 , "Ankush")
b = BankAccount(2000 , "Matre")

a.showbalance()
b.showbalance()

a.deposite(500)
b.deposite(500)








