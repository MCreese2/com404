cover_type = input("What type of cover does the book have? ")
print(cover_type)

if (cover_type == "soft"):
    bound_type = input("Is the book perfect-bound? ")
    print(bound_type)

    if (bound_type == "yes"):
        print("Soft cover, perfect bound books are very popular!")

    elif (bound_type == "no"):
        print("Soft covers with coils or stitches are great for short books")

    else:
        print("I'm sorry, the question is yes or no.")

elif (cover_type == "hard"):
    print("Books with hard covers can be more expensive!")