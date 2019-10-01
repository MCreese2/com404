first_name = input("Confirm your first name: ")
print(first_name)
second_name = input("Confirm your second name: ")
print(first_name, second_name)

if (first_name == "murray") and (second_name == "creese"):
    print("Welcome murray creese, please enter your password to proceed")
    murray_pword = input("Password: ")
    if (murray_pword == "bob"):
        print("Access granted, welcome")
    else:
        print("Password incorrect")

elif  (first_name == "murray") and (second_name != "creese"):
    print("murray, your second name does not match our records")

else:
    print ("Credentials not valid")