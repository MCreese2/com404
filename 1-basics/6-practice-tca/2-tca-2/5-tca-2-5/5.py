health = 100

print("Your health is", str(health) + "%.", "Escape is in progress...")

for count in range (0,5,1):
    who_is = input("...Oh dear, who is that? ")
    print(who_is)

    if who_is.lower() == "smilers's bot":
        health = health - 20
        print("Time to jam out of here!")

    elif who_is.lower() == "hacker":
        print("Yay! Better follow this one!")
        health = health + 20

    else:
        print("Phew, just another emoji!")

print("Escaped! Health is", str(health) + "%.")