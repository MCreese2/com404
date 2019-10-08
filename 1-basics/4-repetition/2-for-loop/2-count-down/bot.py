how_far = int(input("How far are we from the cave? "))
print(how_far, "steps")
print("")
steps_remaining = how_far

for count in range(how_far):
    print(steps_remaining,"steps remaining...")
    steps_remaining = steps_remaining - 1

print("We have reached the cave!")