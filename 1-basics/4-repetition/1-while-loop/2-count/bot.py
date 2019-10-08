#
avoid_cables  = int(input("How many live cables must I avoid? "))
#
print(avoid_cables,"?!")

#
cables_avoided = 0

while cables_avoided < avoid_cables:
    print("Avoiding...")
    cables_avoided = cables_avoided + 1
    print("...Done!",cables_avoided," live cables avoided!")

print("All live cables have been avoided!")