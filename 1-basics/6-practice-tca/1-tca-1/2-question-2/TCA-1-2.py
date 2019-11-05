#Declared a variable and asks for the user's input
forky_status = input("Where if Forky? ")

#Prints the user's response (the forky_status variable)
print(forky_status)

#If statement that prints "Phew!..." if forky_status = specific string
if forky_status.lower() == ("with bonnie"):
    print("Phew! Bonnie will happy.")

#Elif statement that prints "Oh no!..." if forky_status = a specific string
elif forky_status.lower() ==("running away"):
    print("Oh no! Bonnie will be upset!")

#Else statement that prints "Ah!..." for everything else
else:
    print("Ah! I better look for him")