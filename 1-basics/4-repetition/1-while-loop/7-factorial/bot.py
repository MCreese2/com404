user_number = int(input("Please enter a number: "))

# A variable to sum the factotial
factorial = 1

# A variable to count up to the user's number
count  = 1

while count <= user_number:
	factorial = factorial * count
	count = count + 1
 
print("The factorial of", user_number, "is", factorial)


