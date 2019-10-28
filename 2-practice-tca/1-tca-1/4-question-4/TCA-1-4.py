#Defines my function for calling with the "item" parameter
def item_from_suitcase(item):

    print("I wonder what is in my suitcase...")

    #Prints a different message given the input for "item"
    if item.lower() == "toothbrush":
        print("A toothbrush! Well, got to have clean teeth.\n")

    elif item.lower() == "spidey suit":
        print("My Spidey suit! I won't be needing this. I am on holiday.\n")

    else:
        print("An unexpected item! It could be useful.\n")

#Calls the function using three different parameters
item_from_suitcase("toothbrush")
item_from_suitcase("belt")
item_from_suitcase("spidey suit")