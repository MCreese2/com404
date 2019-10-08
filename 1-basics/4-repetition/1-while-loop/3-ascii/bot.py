max_bars = int(input("How many bars should be charged? "))
print(max_bars, "bars!")

bars_charged = 0 

while bars_charged < max_bars:
    # Counter
    bars_charged = bars_charged + 1
    
    # Display
    print("Charged:", ("█" * bars_charged))

print("The battery is fully charged!")
