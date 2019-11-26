
#Asks the user how many miles need to be travelled
how_many_miles = int(input("How many miles must I travel before I reach the secret base? "))

print(how_many_miles)

print("I will count the miles...")
print()

#Displays miles and counts down until 0 is reached
while how_many_miles >= 1:
    print("I have", how_many_miles, "miles to go before I reach the base")
    how_many_miles = how_many_miles - 1

#Prints the final statements, \n is used to display part of the string on a new line
print("I have arrived at the secret headquaters of the MIB!" "\nIt is time to sneak in.")