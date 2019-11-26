#intro
print("Learn the steps of the 5 sequence tango.")

#User provides step number
step_choice = int(input("What step do you want to learn? "))

print(step_choice)

#Provides info based on chosen step
if step_choice == 1:
    print("Leader takes a step back.")

elif step_choice == 2:
    print("Side step towards centre of floor.")

elif step_choice == 3:
    print("Leader steps outside of follower.")

elif step_choice == 4:
    print("Preparation of the cross with the forward step.")

elif step_choice == 5:
    print("Leader closes his feet, follower completes cross step.")

else:
    print("Terminate the sequence.")