# A function is a block of code which only runs when it is called
# You can pass data, known as parameters, into a function


# simple function 
def sum(a, b):
    return a +b

x = sum(2,3)
# print(x)


age = int(input("Please enter your age!: "))

def Ticket_price(age):
    if age >= 13 and age < 18:
        print("Ticket Price is $10")
    elif age >= 18 and age < 25:
        print("Ticket price is $15")
    elif age >= 25 and age < 30:
        print("Ticket price $ 25")
    elif age >=30 and age  <= 50:
        print("Ticket price $30")
    elif age > 50 and age  < 100:
        print("Sorry you are not allowed")
    elif age <13 and age == 1:
        print("Sorry you are not allowed")
    else:
        print("wrong value")


    
Ticket_price(age)