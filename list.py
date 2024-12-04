# Lists are used to store multiple items in a single variable. 
# lists are ordered base they store data in order, it means that the items have a defined order, and that order will not change.
# List items are ordered, changeable, and allow duplicate values. 
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# store multiple data types in the list

list1 = ["apple","mango",1,2,3]
print(list1)

# methods of list
# some of the basic method of the list 
# 1: append()
# this method is used to append the item in the list and this method append in the last of list 

list1.append("ali")

print(list1)

# 2 : extend()
# Adds multiple elements to the end of the list in the form list or in this method you can pass list to add element.

list1.extend(["ahmed",10,23])
print(list1)

# 3: insert()
# Adds an element at a specific position.

list1.insert(2,"imran")
print(list1)

# 4 :remove()
# Removes the first occurrence of an element.

list1.remove("imran")
print(list1)

# 5 : pop()
# they remove the last item of the list

list1.pop()
print(list1)

# 6: del
# Deletes an element at a specified index.

del list1[3]
print(list1)



# food item program through list

food_list = []
flag = True

while flag:
    items = input("Enter your fav food or Q to quit:  ")

    if items == "Q" or items == "q":
        flag = False
        print(food_list)
    else:
        food_list.append(items)


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx