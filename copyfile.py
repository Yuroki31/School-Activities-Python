# Prompt the user for the names of two text files
input_file_name = input("Enter the name of the source text file: ")
output_file_name = input("Enter the name of the destination text file: ")

try:
    # Open the source file for reading
    with open(input_file_name, 'r') as source_file:
        # Read the contents of the source file
        file_contents = source_file.read()

    # Open the destination file for writing
    with open(output_file_name, 'w') as destination_file:
        # Write the contents to the destination file
        destination_file.write(file_contents)

    print(f"File '{input_file_name}' has been copied to '{output_file_name}' successfully.")

except FileNotFoundError:
    print("One or both of the files could not be found. Please check the file names and try again.")

except Exception as e:
    print(f"An error occurred: {e}")
    
#Reading the contents of the files and printing them
f = open("name.txt",'r')
x = open("new.txt",'r')
orig = f.read()
copy = x.read()

print ("\nSource file content:\n" + (orig))
print ("\nDestination file content:\n" + (copy))

