# Initialize variables
tot = 0
count = 0
max_num = None
min_num = None

# Accept input from the user
while True:
    value = float(input("Enter a non-negative number (or a negative number to terminate): "))
    if value < 0:
        break

    # Update variables
    tot += value
    count += 1

    if max_num is None or value > max_num:
        max_num = value

    if min_num is None or value < min_num:
        min_num = value

# Check if any values were entered before computing the average
if count > 0:
    ave = tot / count
    print("Sum: ",tot)
    print("Average: ", ave)
    print("Maximum: ", max_num)
    print("Minimum: ", min_num)

