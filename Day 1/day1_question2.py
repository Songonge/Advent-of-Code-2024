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

#create an empty list where to store the product of the item from the left list to the number of its appearances in the right list.
similarity_values = []
# Iterate through the values in the left list to fill the similarity_values list.
for item in left_list:
    count_value = right_list.count(item) # Count occurrences of i in right_list
    similarity_values.append(item * count_value)
# print(similarity_values)

# Calculate the total similarity score.   
similarity_score = sum(similarity_values)

# Printing the results for similarity_score.
print(similarity_score) 