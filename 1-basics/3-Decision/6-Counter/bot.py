odd_numbers = 0
even_numbers = 0

first_number = int(input("Please enter your first number: "))
print(first_number)
second_number = int(input("Please enter your second number: "))
print(second_number)
third_number = int(input("Please enter your third number: "))
print(third_number)

if (first_number % 2):
    odd_numbers = odd_numbers  +1
else: even_numbers = even_numbers + 1

if (second_number % 2):
    odd_numbers = odd_numbers  +1
else: even_numbers = even_numbers + 1

if (third_number % 2):
    odd_numbers = odd_numbers  +1
else: even_numbers = even_numbers + 1

print("There are ", even_numbers, "even and ", odd_numbers, " odd.")