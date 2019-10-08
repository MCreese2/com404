#Declare the variable for removed cables

#Asks the user to input how many cables to remove
removed_cables = int(input("How many cables should I remove? "))

#Displays the users unput
print(removed_cables, " cables!")

#Declares the variable for counting the cables
cable_count = 0

while cable_count < removed_cables:
    cable_count = cable_count + 1
    print("Removed cable.")

