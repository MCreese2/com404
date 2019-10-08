user_phrase = input("What phrase do you see? ")
print(user_phrase)
print()
print("Reversing...")
word_reverse = str

# /end="" negates the implicit \n which forces the next print onto a new line
print("The phrase reversed is: ", end="")

# starts at the last letter and works backwards
# end="" puts the word onto one line, instead of printing each letter on a seperate line
for position in range(len(user_phrase)-1, -1, -1):
    print(user_phrase[position], end="")