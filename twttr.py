
#implement a program that prompts the user for a str of text and then outputs that same text
#but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

text = input("Enter text:")
result = ""
for letter in text :
    if letter.lower() not in "aeiou":
        result = result + letter 
print(result)        