print("Welcome to the Planet of the Apes...")

#sets counts to 0
ape_count = 0
human_count = 0

#asks ape or human and adds to totals
for count in range(0,7,1):
    human_or_ape = input("...be you human or be ye ape? ")
    print(human_or_ape)

    if human_or_ape.lower() == "human":
        human_count = human_count + 1
        print("I did not start this war. But I will finish it.")

    elif human_or_ape.lower() == "ape":
        ape_count = ape_count + 1
        print("Apes together strong!")

    else:
        print("This is not your fight.")

#Prints totals
print("Total Humans encountered:", human_count)
print("Total Apes encountered:", ape_count)


