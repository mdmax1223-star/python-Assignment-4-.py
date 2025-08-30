# "Write and Append Data to a File"

# Step 1: Take user input and write it to output.txt
user_input = input("Enter some text to write to the file: ")

# Write user input to the file
with open('output.txt', 'w') as file:
    file.write(user_input + '\n')

# Step 2: Append additional data
additional_input = input("Enter additional text to append to the file: ")

with open('output.txt', 'a') as file:
    file.write(additional_input + '\n')

# Step 3: Read and display the final content of the file
with open('output.txt', 'r') as file:
    print("\nFinal content of the file:")
    print(file.read())
