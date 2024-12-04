# tuples
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Tuple items are ordered, unchangeable, and allow duplicate values and store multiple values.



tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)


# Access the element through slicing and index 

print(tuple1[1])

print(tuple1[1:3])

# Unpacking a tuple


fruits = ("apple", "mango","cherry")
(a,b,c) = fruits

print(a)
print(b)
print(c)

# loop on tuple 

for i in fruits:
    print(i)


# food menu program using tuple 
food_menu = ("Pizza", "Burger", "Pasta", "Salad", "Juice")


print("Food Menu:")
for item in food_menu:
    print(f"- {item}")


print("\nThe first item on the menu is:", food_menu[0])
print("The last item on the menu is:", food_menu[-1])


new_food_menu = food_menu + ("Coffee",)
print("\nUpdated Food Menu:")
for item in new_food_menu:
    print(f"- {item}")


print("\nThe first three items on the menu are:")
print(new_food_menu[:3])


food_to_find = "Pasta"
if food_to_find in new_food_menu:
    print(f"\n{food_to_find} is available on the menu!")
else:
    print(f"\n{food_to_find} is not available on the menu.")
