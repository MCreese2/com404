def is_league_united(first_hero, second_hero):
    if (first_hero.lower() == "superman" and second_hero.lower() == "wonder woman") or (first_hero.lower() == "wonder woman" and second_hero.lower() == "superman"):        
        return True

    else:
        return False

def decide_plan(first_hero, second_hero):
    is_league_united(first_hero, second_hero)

    if is_league_united(first_hero, second_hero) == True:
        print("Time to save the world!")

    elif is_league_united(first_hero, second_hero) == False:
        print("We must unite the league!")

def run():
    first_hero = input("Enter the first hero: ")
    second_hero = input("Enter the second hero: ")

    league_or_plan = input("League or Plan? ")

    if league_or_plan.lower() == "league":
        is_league_united(first_hero, second_hero)
        if is_league_united(first_hero, second_hero) == True:
            print("True")
        
        else:
            print("False")

    elif league_or_plan.lower() == "plan":
        decide_plan(first_hero, second_hero)

    else:
        print("Invalid command. Please try again")

run()