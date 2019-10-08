bright_level = int(input("What level of brightness is required? "))
print(bright_level)

print("")
print("Adjusting brightness...")
print("")

# Brightness always starts at 2, so this variable is displayed before the loop begins
display_bright = 2
print("Beep's brightness level:", ("X" * display_bright))
print("Bop's brightness level:", ("X" * display_bright))
print("")

# range(2-starts at 2, bright_level-end at user input, 2-in increments of 2)
for count in range(2, bright_level, 2):
    print("Beep's brightness level:", ("X" * (display_bright + count)))
    print("Bop's brightness level:", ("X" * (display_bright + count)))
    print("")

print("Adjustments Complete!")