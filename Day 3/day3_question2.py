# Import the re module to identify valid expressions in the corrupted file.
import re

# Open the file and read its content line by line.
with open('input_day_3.txt', 'r') as f:
    lines = f.read()

# Define a function to check each line and locate the correct multiplications expression
def total_valid_mul_control_exp(file_content):
    valid_pattern = r"mul\((\d+),(\d+)\)"  # The lower case 'r' tells Python to interpret the string 
                                           # as a raw string, exactly as I've typed it. 

    check_pattern = r"(do\(\)|don't\(\))"  # Check for do() or don't() on each line.

    # Set a condition needed to consider a mul() expression. 
    enabled = True
    total_sum = 0  # Initiatize the sum to zero

    # Split each line in the file content into parts based on given instructions.
    matched_pattern = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", file_content)

    # Necessary loop to keep or not keep the mul() expression.
    for line in matched_pattern:
        if line == "do()":
            enabled = True  # keep the following mul() expression.
        elif line == "don't()":
            enabled = False  # Do not keep the following mul() expression.
        elif enabled and line.startswith("mul"):  # Proceed if enabled is True.
            i, j = map(int, re.findall(r"\d+", line)) # Extract the numbers in the mul() expression.
            total_sum += i * j  # Add the product of the two numbers to the total sum.
            
    return total_sum

# Use the function above-defined to calculate the sum of all valid expressions 
# in the input file based on the new instructions.
result = total_valid_mul_control_exp(lines)

# Print the result of the sum.
print(result)
