user_markings = input("What strange markings do you see? ")

index_number = 0

for position in range(0, len(user_markings), 1):
    print("index", str(index_number) + ":", user_markings[position])
    index_number = index_number + 1

print()
print("Done!")