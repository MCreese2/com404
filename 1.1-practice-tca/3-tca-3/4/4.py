#spideySense function
def spideySense(enemy, direction):

    #provides different responses given the parameters
    if enemy == "Green Goblin":
        print("Goblin bombs incoming from", end=" ")

    elif enemy == "Venom":
        print("Venomous webbing incoming from", end=" ")

    elif enemy == "Electro":
        print("Electro striking from", end=" ")

    else:
        print("New enemy attacking from", end=" ")

    print(direction)

#calls the function with various parameters
spideySense("Green Goblin", "front")
spideySense ("Venom", "behind")
spideySense ("Electro", "left side")
spideySense ("Unknown", "right side")