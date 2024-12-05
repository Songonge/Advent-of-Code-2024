# Open the file named input_day_1.txt and read lines in it.
with open('input_day_1.txt', 'r') as f:
    lines = f.readlines()

# Create two empty lists where to strore vales from each column in the file.
left_list = []
right_list = []

# Iterate through each line in the file   
for line in lines:
    column1, column2 = line.split() # Use split() to split each line in two parts by space.
    # Append the values for each list into the empty lists created above.
    left_list.append(int(column1))
    right_list.append(int(column2))

    # Print the results for each list.
    print(left_list)
    print(right_list)

# Sort each list from by ascending.
left_list.sort()
right_list.sort()
#create an empty list where to store the difference between the matched values from the two lists.
matched_values = []
# Iterate through the values in each list to fill the matched_values list.
for value_l, value_r in zip(left_list, right_list):
    matched_values.append(abs(value_l - value_r)) # Store the difference in the matched_values list.

# Initialize the total distance between matched values to zero.
total_distance = 0
# Use a for loop to sum all the differences between matched values.
for value in matched_values:
    total_distance += value

# Printing the results for matched values and the total distance.
print(matched_values)
print(total_distance)
