def display_in_box(word):
    print("*" * (len(word) + 10))
    print("*", word, "*")
    print("*" * (len(word) + 10))

def display_in_lower(word):
    print(word.lower())

def display_in_upper(word):
    print(word.upper())

def display_mirrored(word):
    print(word, " | ")
    for position in range(len(word)-1, -1, -1):
        print(word[position], end="")

def display_repeat(word):
    display_no = int(input("How many times shall I display the word? "))
    for x in range(0, display_no):
        if (x % 2):
            print(word.upper())
        else:
            print(word.lower())

def user_input():
    word = input("Please enter a word: ")
    print("""Options: \n
    1) Display in a Box \n
    2) Display Lower-case \n
    3) Display Upper-case \n
    4) Display Mirrored \n
    5) Repeat""")
    decision = input("Please pick an option... ")


    if decision == "1":
        (display_in_box(word))

    elif decision == "2":
        (display_in_lower(word))

    elif decision == "3":
        (display_in_upper(word))

    elif decision == "4":
        (display_mirrored(word))

    elif decision == "5":
        (display_repeat(word))

user_input()