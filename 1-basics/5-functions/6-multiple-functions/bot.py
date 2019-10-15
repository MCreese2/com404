def display_ladder(steps):
    print("""| |
*** \n""" * int(steps))

def create_ladder():
    steps = input("How many steps remaining? ")
    print(steps)
    display_ladder(steps)

create_ladder()