## overheads.py
## will be used as a module

## import required modules
from pathlib import Path
import csv

fp_read = Path.cwd()/"csv_reports"/"overheads.csv"
# print(fp_read.exists())

with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    # create empty lists to store data
    overheads = []
    
    for row in reader:
        overheads.append([row[0],row[1]]) 

# print(overheads)

values = []
for value in overheads:
    # convert stings into a float 
    value[1] = float(value[1])
    
    values.append(value[1])
    
# Find the highest value from the float values
highest_value = max(values)
# print(highest_value)

for i , value in enumerate(values):
    if value == highest_value:
        name = overheads[i][0]
    break

# Print the highest overhead and its corresponding value
summary_overheads = f'[HIGHEST OVERHEADS] {name}: {highest_value}%'
print(summary_overheads)

def write_to_file(filename, content):
    fp_write = Path.cwd()/"summary_report.txt"
    fp_write.touch()
    with fp_write.open(mode="w", encoding="UTF-8" ) as file:
        file.write(summary_overheads)