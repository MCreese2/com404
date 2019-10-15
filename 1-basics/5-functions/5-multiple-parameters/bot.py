def climb_ladder(s_remain, s_crossed):
    if s_remain < s_crossed:
        print("Still some Way to go!")
    else:
        print("We Made it!")

climb_ladder(2, 5)
climb_ladder(5, 5)