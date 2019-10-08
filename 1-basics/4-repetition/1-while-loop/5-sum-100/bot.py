print("Calculating the sum of the first 100 numbers...")

# A variable to count from 1 to 100
sum_count = 0

# A variable that tracks the sum of each number
result = 0

while sum_count < 100:
    sum_count = sum_count + 1
    # the result is totaled by adding sum count to result at each iteration
    result  = result + sum_count

print("...Done! the answer is", result)