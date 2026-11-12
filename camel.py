
#implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. 
# Assume that the user’s input will indeed be in camel case.

camel = input("firstname lastname")
snake = " "
for character in camel:
    if character.isupper():
        snake += "_"+ character.lower()
    else:
         snake += character




print (snake)