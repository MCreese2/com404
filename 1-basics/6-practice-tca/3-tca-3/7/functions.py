def ASCII(five_digit):
    print("""*
**
***
****
*****
******
*******
********
*""",five_digit,"""*
**********""")

def left_triangle(five_digit):
    total = ""
    for count in str(five_digit):
        total = total + count
        print(total)

def right_triangle(five_digit):
    total = ""
    for count in str(five_digit):
        total = total + count
        print(total.rjust(5))
