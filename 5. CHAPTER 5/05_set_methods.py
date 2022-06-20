##Creating an empty set
b = set()
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5)
b.add(5)# Adding a value repetedly does not update or change a set.
print(b) # returns {4, 5} only because, set is a collection on non repetative elements.
# b.add([4, 5, 6]) # cannot add list because it can be changed because it is unhashable
# print(b)
b.add((4, 5, 6)) # Tuple can be added.
print(b)
# b.add({4:5}) # cannot add dictionary to sets

##Length of the set
print(len(b)) # Prints the length of the set

##Removal of an Item
b.remove(5) # Removes 5 from set b
b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(b)