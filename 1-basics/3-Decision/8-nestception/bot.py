look_where = input("Where should I look (bedroom, bathroom or lab)? ")
print("in the ",look_where)

if (look_where == "bedroom"):
    bedroom_where = input("Where in the bedroom shall I look? ")
    print(bedroom_where)
    if (bedroom_where == "under the bed"):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")

if (look_where == "bathroom"):
    bathroom_where = input("Where in the bathroom shall I look? ")
    print(bathroom_where)
    if (bathroom_where == "in the bathtub"):
        print("Found a rubber duck but no battery")
    else:
        print("It is wet but I found no battery.")

if (look_where == "lab"):
    lab_where = input("Where in the lab shall I look? ")
    print(lab_where)
    if (lab_where == "on the table"):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")