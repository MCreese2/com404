#declares a variable for the user to input a string and reads it back
user_phrase = input("Please enter a phrase: ")
print(user_phrase)

#declares the variable for the loop
bop = 0

#counts +1 bop until bop = the number of letters in the phrase 
#len() counts the number of objects within the brackets
while bop < len(user_phrase):
    bop = bop + 1

#breaks the loop by printing "bop" for every bop
print("bop " * bop)
