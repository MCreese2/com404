
def cross_bridge(distance):
    for count in range(distance):
        print("Crossed step")

    if distance > 5:
        print("The bridge is collapsing!")

    else:
        print("We must keep going!")

cross_bridge(3)
cross_bridge(6)