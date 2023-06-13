import re
import csv

# Read the data from the file
FILENAME = "pindelay.txt" # Change as needed!!
NumPinsPerRow = 23 # Package dependent, change as needed

with open(FILENAME, 'r') as file:
    data = file.readlines()

# Define a function to extract the letter and number from each line
def extract_letter_and_number(line):
    match = re.match(r'([A-Z]*)(\d+)', line, re.I)
    if match:
        items = match.groups()
        return items[0] if items[0] else 'A', int(items[1])
    return None, None

# Convert the data into a dictionary for easy lookup
data_dict = {}
for line in data:
    key, num = extract_letter_and_number(line)
    if key is not None:
        fields = line.strip().split(' ')
        # Divide the second field by 1000
        fields[1] = str(float(fields[1]) / 1000)
        data_dict[key+str(num)] = fields

# Generate the complete sequence
letters = sorted(set(key for key, num in map(extract_letter_and_number, data) if key is not None))
complete_data = []
for letter in letters:
    for num in range(1, NumPinsPerRow):
        key = letter + str(num)
        if key in data_dict:
            complete_data.append(data_dict[key])
        else:
            complete_data.append([key, '0'])

# Write the complete data to a new CSV file
with open('complete_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in complete_data:
        writer.writerow(row)
