#Asks the user how many cables need to be avoided
avoid_cables  = int(input("How many live cables must I avoid? "))

#Prints the user's input back to them
print(avoid_cables,"?!")

#Declares variable to count no. of cables avoided
cables_avoided = 0

#Loop to trigger if the no. of cables avoided is less than that stated by the user
while cables_avoided < avoid_cables:
    print("Avoiding...")
    cables_avoided = cables_avoided + 1
    print("...Done!",cables_avoided," live cables avoided!")

#Displays message when the user's number is met.
print("All live cables have been avoided!")