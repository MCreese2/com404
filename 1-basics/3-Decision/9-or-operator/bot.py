adventure_type = input("What type of adventure should we go on (scary, short, long or safe)? ")
print(adventure_type)

if (adventure_type == "short") or (adventure_type == "scary"):
    print("Entering the Dark Forest")

elif (adventure_type == "safe") or (adventure_type == "long"):
    print("taking the safe route home!")