# conditional statements is used to check which condition is true and which condition is false 

a = 7
b = 7

if a > b:
    print("A is greater then B")
elif b > a:
    print("B is greater the A")
else:
    print("Both A and B are same")


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



# program to check the ticket price base on age in a family park

age = int(input("Please enter your age!: "))




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




