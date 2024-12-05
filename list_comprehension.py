# list comprehension
# this is syntax to make list comprehension


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist= [x for x in fruits]
print(newlist)

b = [x if x != "banana" else "orange" for x in fruits]
print(b)



a = [x**2 if x % 2 == 0 else x**3 for x in range(1,16)]

print(a)


