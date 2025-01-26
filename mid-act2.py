# Open the file
file_name = input ("Enter the name of the text file: ")
with open(file_name, 'r') as file:
    # Read the lines and convert them to a list of integers
    lines = file.readlines()
    integers = [int(line.strip()) for line in lines]

    # Calculate the average
    if integers:
        average = sum(integers) / len(integers)
        f = open(file_name, 'r')
        dis = f.read()
        print ("\nSource file content:\n" + (dis))
        print(f'The average value of the integers is: {average}')
    else:
        print("The file is empty.")

