'''Write a program to create a dictionary of Hindi words with value as their
english translation. Provide user with an option to look it up!'''

myDict = {
    "pankha" : "Fan",
    "Dabba" : "Box",
    "vastu": "item"
}
print("options are", myDict.keys())
a = input("Enter the Hindi word\n")
# print("The meaning of your word is:", myDict[a])

# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))
