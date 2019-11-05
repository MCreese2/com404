zones_to_cross = int(input("How many zones must I cross? "))

print(zones_to_cross)

print("crossing zones...")

while zones_to_cross >= 1:
    print("crossed zone", zones_to_cross)
    zones_to_cross = zones_to_cross - 1

print("\nCrossed all zones. Jumanji!")
