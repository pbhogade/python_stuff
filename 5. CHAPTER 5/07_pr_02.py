'''Write a program to input eight numbers from the user and 
display all the unique number once
'''
num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n"))
num3 = int(input("Enter number 3\n"))
num4 = int(input("Enter number 4\n"))
num5 = int(input("Enter number 5\n"))
num6 = int(input("Enter number 6\n"))
num7 = int(input("Enter number 7\n"))
num8 = int(input("Enter number 8\n"))
print("you have entered these numbers as follows\n", (num1, num2, num3, num4, num5, num6, num7, num8))
s = {num1, num2, num3, num4, num5, num6, num7, num8}
print("unique numbers are \n", s)
