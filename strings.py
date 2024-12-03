# strings

# strings are used in double quotes or single qoutes and for the paragraph can use triple qoutes and save in variable

# single quotes
single_quotes = 'this is single qoutes string'

# double quotes
double_quotes = "THIS IS DOUBLE QOUTES STRING"

# paragraph

paragraph = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""


print(single_quotes)
print(double_quotes)
print("\n")
print(paragraph)

# strings Methods
# all these are used with string and used with . and ()

# 1 capitalize()
# this method is to make first letter of string capital
print(single_quotes.capitalize())

# 2 upper()
# this method is to make a all string in upper case 
print(single_quotes.upper())

# 3 lower()
# this method makes all the characters of string in lower case 
print(double_quotes.lower())

# 4 lstrip()
# this method is used to allign the string on left side and removes all the spaces from left side
single_quotes = '    this is single qoutes string'


print(single_quotes.lstrip())


# 4 rstrip()
# this method is used to allign the string on right side and remove all the space on the right side
single_quotes = 'this is single qoutes string          '
print(single_quotes.rstrip())


# 5 strip()
# this method is used to remove  the spaces from left side or right side of the string
single_quotes = '       this is single qoutes string          '

print(single_quotes.strip())

# 6 title()
# this method Converts the first character of each word to upper case
single_quotes = 'this is single qoutes string'

print(single_quotes.title())

# 7 replace()
# Returns a string where a specified value is replaced with a specified value

print(single_quotes.replace('single', 'double'))

# 8 find()
# Searches the string for a specified value and returns the position of where it was found

print(single_quotes.find("is"))


# 9 join()
# this method is used to join and make a string
mylist = ["John", "Peter", "Vicky"]
a = " ".join(mylist)
print(a)


# 10 split()
# this method is used to split the string and make a list

txt = "welcome to the jungle"

b = txt.split()
print(b)



# Escape Characters
print("escape charaters are \n used with a string")
print("escape charaters \'are\' used with a string")
print("escape charaters \\are\\ used with a string")
print("escape charaters \t are used with a string")
print("escape charaters \rare used with a string")


# String Concatenation

a = "Hello"
b = "World!"
print(a + b)
print("\n")
print(a + " " + b)



# slicing and indexing 

single_quotes = 'this is single qoutes string'


# slicing

print(single_quotes[0:6])
print(single_quotes[0:12:2])
print(single_quotes[::3])
print(single_quotes[-1:-10:-1])




# indexing
print(single_quotes[0])
print(single_quotes[1])
print(single_quotes[5])
