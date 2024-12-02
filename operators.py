# Arithmetic Operators 


a = 10
b = 30

# Addition
print(a + b)

# Subtraction
print(a - b)

# Multiplication
print(a * b)

# Division
# there are two type of divisions in python
# 1 float division / floor division
print(a / b)

# 2 integer division 
print(a // b)

# Modulus 
print(a%b)


# Exponentiation 
print(a**b)


# Comparison Operators
# these operators are used to compare statements with each other

# 1 : == (equal) this operator is to check comparision between two statements

if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b") 

a = 10
b= 20
# 2 != (not equal to) if two vales are not equal to each other they return true and if equal they retrun false
if a != b:
    print("a is not equal to b")
else:
    print("a equal to b") 

# 3 > (greater then) this is to check the which value is greater then the other value
if a > b:
    print("a greater then b")
else:
    print("a is less then  b") 


# 4 Less than  
if a < b:
    print("a less then b")
else:
    print("a is not less then  b")


# 5 >= greater then equal to

if a >= b:
    print("statement A")
else:
    print("statement B")

# 6 <= less than or equal to 
if a <= b:
    print("statement A")
else:
    print("statement B")




#  Logical Operators


# 1 and they return true if both statements are true


x = 10


if (x > 5) and (x < 15 ):
    print("statement 1 is running")
else:
    print("statement 2 is running")


# 2 or they return true if one statement is true

if (x>10) or (x<15):
    print("statement 1 is running")
else:
    print("statement 2 is running")


# 3 not  reverse the result if statement is true then return false

if (not(x > 3 and x < 10)):
    print("statement 1 is running")
else:
    print("statement 2 is running")



# in operator

list_1 = ["apple", "banana", "cherry"]

if "apple" in list_1:
    print("this is availabe in the list")
else:
    print("not available")