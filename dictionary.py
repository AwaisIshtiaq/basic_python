# A Python dictionary is a data structure that stores the value in key: value pairs. Values in a dictionary can be of any data type
# and can be duplicated, whereas keys can’t be repeated and must be immutable.


# Create dictionary

data = {
    "name":"ALi",
    "age":26,
    "country":"Pakistan"
}

print(data)

# Adding and Updating Dictionary Items 


data["degree"] = "Bs computer science"

print(data)

data["age"] = 28

print(data)


# Removing Dictionary Items
del data["age"]


print(data)

a = data.pop("name")

print(a)


# Iterating Through a Dictionary
# iterate over key 


for key in data:
    print(key)

# iterate over values 


for values in data.values():
    print(values)


# iterate both key and values 

for key, values in data.items():
    print(f"key : {key} and values : {values}")


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


# shopping cart program store in dictionary


shopping_cart = {}


shopping_cart["apple"] = 2  
shopping_cart["banana"] = 5  
shopping_cart["orange"] = 3  


print("Shopping Cart Contents:")
for item, quantity in shopping_cart.items():
    print(f"{item.capitalize()}: {quantity}")
