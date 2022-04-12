from decimal import DivisionImpossible
from re import L, S
from tokenize import Exponent


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight)/float(height)**2
bmi_as_int = int(bmi)
print(bmi_as_int)

# here we have learned mathametical operations and type casting
#PEMDAS LR
# P = perentises
# E = Exponent
# M = multiplication
# D = Division
# A = Addition 
# S = substraction
# LR= Left------>right 
