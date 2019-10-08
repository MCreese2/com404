max_bars = int(input("How many bars should be charged? "))
print(max_bars, "bars!")

bars_charged = 0 

while bars_charged < max_bars:
    # counter
    bars_charged = bars_charged + 1
    
    # stack
    bars = "█" * bars_charged
    
    #Display
    print("Charged:", bars)

print("The battery is fully charged!")
