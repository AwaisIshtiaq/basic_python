# A set is a collection which is unordered, unchangeable*, and unindexed. 

myset = {"apple", "banana", "cherry"}
print(myset)


# adding in sets 

myset.add("mango")

print(myset)



# iterte over sets 


for i in myset:
    print(i)


# removing items form set 

# 1: romove()
myset.remove("mango")
print(myset)

# 2: pop()
myset.pop()

print(myset)


# 3: clear()


myset.clear()

print(myset)
