# Dictionary Methods 
mydict = {
    "fast": "In a quick manner",
    "praveen": "A Coder",
    "marks": [1,2,5],
    "anotherdict": {'harry': 'Player'},
    1:2
}
# print(mydict.keys()) # Prints the keys of dictionary.
# print(type(mydict.keys())) # we can get the type of this (by default)
# print(list(mydict.keys())) # we can change the type into list. (typecast)
# print(mydict.values()) # print the values.
# print(mydict.items()) # prints the (key, value) for all contents of the dictionary
print(mydict)
updatedict = {
    "lovish": "friend",
    "praveen": "dancer" # This will update the existing value.
}
mydict.update(updatedict) # Updates the dictionary by adding key-value pairs from updatedict
print(mydict)
print(mydict.get("praveen2")) # Returns None as harry is not present in the dictionary
print(mydict.get["praveen2"]) # throws an error as harry is not present in the dictionary