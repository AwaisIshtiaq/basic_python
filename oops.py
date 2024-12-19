# simple class example

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
miles = Dog("Miles", 4, "Jack Russell Terrier")

jack = Dog("Jack", 3, "Bulldog")





# example 2 simple atm machine
class ATM:
    __counter = 1


    def __init__(self):
        

        # encapsulation mean to hide some part of data in you code to you this __ to hide the data you want
        self.__pin = ""
        self.__balance = 0
        # print(id(self))
        self.sno = ATM.__counter
        ATM.__counter = ATM.__counter + 1


        self.menu()


    @staticmethod
    def get_counter():
        return ATM.__counter

    @staticmethod
    def set_counter(new):
        if type(new) == int:
            ATM.__counter  = new
        else:
            print("Not Allowed")


    def get_pin(self):
        return self.__pin
    def set_pin(self, new_pin):

        if type(new_pin) == str:
            self.__pin = new_pin
            print("Pin change")
        else:
            print("Not Allowed")

    def menu(self):
        user_input = input("""
                        Hello, How would you like to proceed?
                        1.Enter 1 to create pin.
                        2.Enter 2 to deposit.
                        3.Enter 3 to withdraw.
                        4.Enter 4 to Check balance.
                        5.Enter 5 to Exit.
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input =="4":
            self.check_balance()
        else:
            print("Bye")

    def create_pin(self):
        self.__pin = input("Enter your pin : ")
        print("pin set sucessfully")

        self.menu()

    def deposit(self):
        temp = input("Enter Your pin")
        if temp == self.__pin:
            amount = int(input("Enter You deposited amount : "))
            self.__balance = self.__balance + amount
            print("Deposit Sucessfully")
        else:
            print("Invalid pin")
        
        self.menu()


    def withdraw(self):
        temp = input("Enter Your pin")
        if temp == self.__pin:
            amount = int(input("Enter You withdraw amount : "))

            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print("Operation Sucessfull")
            else:
                print("Insufficient balance")
        else:
            print("Invalid Pin")
        
        self.menu()


    def check_balance(self):
        temp = input("Enter Your pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid Pin")

        self.menu()


c1 = ATM()

c2= ATM()
