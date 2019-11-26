
def run():
    five_digit = int(input("Please enter a five digit number: "))
    option_choice = int(input("Please select one of the following three options...\n1. ASCII\n2. Left Triangle\n3. Right Triangle\n"))
    print(five_digit)
    print()

    if option_choice == 1:
        from functions import ASCII
        ASCII(five_digit)

    elif option_choice == 2:
        from functions import left_triangle
        left_triangle(five_digit)

    elif option_choice == 3:
        from functions import right_triangle
        right_triangle(five_digit)

    else:
        print("Invalid option.")

run()