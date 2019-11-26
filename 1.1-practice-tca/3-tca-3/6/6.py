#check if slugs are the same
def isFusionShot(slug_type_1, slug_type_2):
    if slug_type_1 == slug_type_2:
        return True

    else:
        return False

#Check if defective shot applies
def isDefectiveShot(slug_type_1, slug_type_2):
    if  (isFusionShot(slug_type_1, slug_type_2) == False) and (slug_type_1.lower() == "infurnus" and slug_type_2.lower() == "aquabeek") or (slug_type_2.lower() == "infurnus" and slug_type_1.lower() == "aquabeek"):
        return True

    else:
        return False

#The interface/menu
def run():
    slug_type_1 = input("Please enter first slug type: ")
    slug_type_2 = input("Please enter second slug type: ")

    fusion_or_defective = input("Please enter fusion or defective: ")

    if fusion_or_defective.lower() == "fusion":

        if isFusionShot(slug_type_1, slug_type_2) == True:
            print("Fusion True")

        else:
            print("Fusion False")


    elif fusion_or_defective.lower() == "defective":

        if isDefectiveShot(slug_type_1, slug_type_2) == True:
            print("Defective True")

        else:
            print("Defective False")

    else:
        print("Invalid selection. Please try again.")

#calls the program
run()

