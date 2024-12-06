"""
Opening the file to read each line in the file.
"""
with open('input_day_2.txt', 'r') as f:
    lines = f.readlines()

# Check if the levels on each line in lines are either strictly increasing or strictly decreasing and 
# verifie that the difference between adjacent levels is between 1 and 3.
def is_safe(report):
    levels = list(map(int, report.split()))
    # Check if all adjacent differences are within 1 to 3 and the sequence is monotonic
    differences = [j - i for i, j in zip(levels, levels[1:])]
    if all(1 <= abs(item) <= 3 for item in differences) and (all(item > 0 for item in differences) or all(item < 0 for item in differences)):
        return True

    return False

# Check if the levels on each line in lines are either strictly increasing or strictly decreasing and 
# verifie that the difference between adjacent levels is between 1 and 3. Then, check if the report 
# becomes safe after removing a single level from the report.
def become_safe(report):
    levels = list(map(int, report.split()))

    if is_safe(report):
        return True
    
    for i in range(len(levels)):
        new_report = levels[:i] + levels[i+1:]
        if is_safe(" ".join(map(str, new_report))):
            return True
    return False

# Counts how many reports in the input list become safe and return the number.
def count_become_safe_reports(value):
    return sum(become_safe(report) for report in value)

# Calculate and print the number of reports that became safe from the lines.
become_safe_reports = count_become_safe_reports(lines)
print(f"Number of safe reports: {become_safe_reports}")