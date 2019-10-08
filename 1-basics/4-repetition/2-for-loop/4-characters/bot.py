user_markings = input("What strange markings do you see? ")

index_number = 0

# Position executes the for statement for each letter in the input
for position in range(0, len(user_markings), 1):
    # this displays an index number counter + the letter of the current position in the for loop
    print("index", str(index_number) + ":", user_markings[position])
    index_number = index_number + 1

print()
print("Done!")