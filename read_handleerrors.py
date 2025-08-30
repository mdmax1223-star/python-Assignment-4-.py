# Task 1: Read a File and Handle Errors

try:
    # Try to open and read the file
    with open('sample.txt', 'r') as file:
        # Read and print each line of the file
        for line in file:
            print(line.strip())  # strip to remove any extra newlines
except FileNotFoundError:
    # Handle the case where the file does not exist
    print("The file 'sample.txt' does not exist.")
