# for loops
# for loop is used to itrateiterating. you can iterate over list, tuple, dictionary, set ,string 
# also you use with range

for i in range(5):
    print("Hello")


fruits_list = ["apple", "cherry","banana","mango"]

for i in fruits_list:
    print(i)

a = "apple"

for i in a:
    print(i)



table = int(input("enter a table Number: "))

for i in range(1,11):
        print(f"{table} x {i} = {table*i}")



# while loop 

# With the while loop we can execute a set of statements as long as a condition is true.

a = 1

while a < 5:
    print("Hello")
    a += 1


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


i = 1
while i < 6:
  i += 1
  print(i)
  if i == 3:
    continue