bright_level = int(input("What level of brightness is required? "))
print(bright_level)

print("")
print("Adjusting brightness...")
print("")

display_bright = 2
print("Beep's brightness level:", ("X" * display_bright))
print("Bop's brightness level:", ("X" * display_bright))
print("")

for count in range(2, bright_level, 2):
    print("Beep's brightness level:", ("X" * (display_bright + count)))
    print("Bop's brightness level:", ("X" * (display_bright + count)))
    print("")

print("Adjustments Complete!")