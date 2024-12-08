# Import the re module to identify valid expressions in the corrupted file.
import re

# Open the file and read its content line by line.
with open('input_day_3.txt', 'r') as f:
    lines = f.read()

# Define a function to check each line and locate the correct multiplications expression
def total_valid_mul_exp(file_content):
    valid_pattern = r"mul\((\d+),(\d+)\)"  # The lower case 'r' tells Python to interpret the string 
                                           # as a raw string, exactly as I've typed it.

    # Find all matched patterns in the file content.
    matched_pattern = re.findall(valid_pattern, file_content)

    # Calculate the total sum of all valid multiplication expressions.
    total_sum = 0
    for i, j in matched_pattern:
        total_sum += int(i) * int(j)

    return total_sum

# Use the function above-defined to calculate the sum of all valid expressions in the input file.
result = total_valid_mul_exp(lines)

# Print the result of the sum.
print(result)
