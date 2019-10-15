def sum_weights(beep_weight, bop_weight):
    total_weight = int(beep_weight) + int(bop_weight)
    return total_weight

def calc_avg_weight(beep_weight, bop_weight):
    avg_weight = int(beep_weight) + int(bop_weight) / 2
    return avg_weight

def run():
    beep_weight = input("How much does beep weigh? ")
    print(beep_weight)
    bop_weight = input("How much does bop weigh? ")
    print(bop_weight)
    decision = input("avg or sum? ")
     
    if decision == "avg":
        print(calc_avg_weight(beep_weight, bop_weight))

    elif decision == "sum":
        print(sum_weights(beep_weight, bop_weight))

run()