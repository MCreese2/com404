user_phrase = input("What phrase do you see? ")
print(user_phrase)
print()
print("Reversing")
print()

result = ""

for letter in user_phrase:
    result = letter + result

print(result)