print("What is your name?")
user_name = input()
print("what is your age? (years)")
user_age = int(input())
print("what is your height? (meters)")
user_height = float(input())
print("what is your weight? (Kilograms)")
user_weight = float(input())
print("")
print(user_name + ", you are " + str(user_age) + " years old and your bmi is " + str(user_weight / (user_height*user_height)))
