
#implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer
# Assume that the user will input an integer.

input = int(input("Enter mass:"))
c = 300000000
E = input*c**2
print(E)