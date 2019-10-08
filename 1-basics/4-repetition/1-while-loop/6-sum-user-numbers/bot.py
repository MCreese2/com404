numbers_to_sum = int(input("How many numbers should I sum up? "))
print(numbers_to_sum)

# Variable to display which number is being entered
numbers_received = 1

# Variable to sum the numbers input
number_sum = 0

while numbers_received <= numbers_to_sum:
    print("Please enter number", numbers_received, "of", str(numbers_to_sum) + ":")
    numbers_received = numbers_received + 1
    number_sum = number_sum + int(input())

print("The answer is:" + str(number_sum))
