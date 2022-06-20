'''Create an empty dictionary. Allow 4 friends to enter their favourite language 
as values and use keys as their names.Assume that the names are unique'''

favLang = {}
a = input("Enter your favourite language Sagar\n")
b = input("Enter your favourite language Manoj\n")
c = input("Enter your favourite language Omshankar\n")
d = input("Enter your favourite language Rakesh\n")
favLang["Sagar"] = a
favLang["Manoj"] = b 
favLang["Omshankar"] = c 
favLang["Rakesh"] = d
print(favLang)