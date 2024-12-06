"""
Opening the file to read each line in the file.
"""
with open('input_day_2.txt', 'r') as f:
    lines = f.readlines()

# Check if the levels on each line in lines are either strictly increasing or strictly decreasing and 
# verifie that the difference between adjacent levels is between 1 and 3.
def is_safe(report):
    # Convert the report to a list of integers
    levels = list(map(int, report.split()))
    # Check if all adjacent differences are within 1 to 3 and the sequence is monotonic
    differences = [j - i for i, j in zip(levels, levels[1:])]
    return all(1 <= abs(item) <= 3 for item in differences) and (all(item > 0 for item in differences) or all(item < 0 for item in differences))

# Counts how many reports in the input list are safe and return the number of safe reports.
def count_safe_reports(value):
    return sum(is_safe(report) for report in value)

# Calculate and print the number of safe reports
safe_reports = count_safe_reports(lines)
print(f"Number of safe reports: {safe_reports}")
