first_number = int(input("Please enter the first number: "))
print(first_number)
second_number = int(input("Please enter the second number: "))
print(second_number)
if (first_number < second_number):
    print("The first number is the smallest.")
elif (second_number < first_number):
    print("The second number is the smallest.")
elif (first_number == second_number):
    print("The numbers are equal.")
print("Done.")