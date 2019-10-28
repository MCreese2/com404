#user inputs number of heroes to gather
gather_heroes = int(input("How many heroes must we gather? "))

print(gather_heroes)

print("Gathering heroes...")

#sets the counter to 1
hero_count = 1

#counts up to number of heroes entered and displays a message each time
while hero_count <= gather_heroes:
    print("...found hero", hero_count)
    hero_count = hero_count + 1

print("...all heroes have been gathered")