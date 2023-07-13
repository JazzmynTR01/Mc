## profit_loss.py
## will be used as a module

## import required modules
from pathlib import Path
import csv

fp_read = Path.cwd()/"csv_reports"/"profit and loss.csv"
# print(fp_read.exists())

with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    # create empty lists to store data
    pl = []
    
    for row in reader:
        pl.append([row[0],row[4]])

# print(pl)

def is_list_increasing(lst):
    for i in range(1, len(lst)):
        if lst[i] <= lst[i-1]:
            return False
    return True

# If cash is always higher than the previous day, the code will give the cash surplus
if is_list_increasing(pl):
    result = "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
    
    def calculate_highest_surplus(data):
        highest_surplus = 0
        previous_value = None
        day_with_highest_surplus = None
        
        for entry in data:
            day = entry[0]
            value = float(entry[1])
            
            if previous_value is not None:
                surplus = value - previous_value
                if surplus > highest_surplus:
                    highest_surplus = surplus
                    day_with_highest_surplus = day
                
            previous_value = value
        
        return day_with_highest_surplus, highest_surplus

    day, highest_surplus = calculate_highest_surplus(pl)
    result += f"[HIGHEST NET PROFIT SURPLUS] DAY {day}, AMOUNT: USD{highest_surplus:.0f}\n"

# This function will then calculate and store the deficits
else:
    result = ""
    
    def calculate_deficit(data):
        previous_value = None
        deficit_result = []
        
        for entry in data:
            day = int(entry[0])
            value = int(entry[1])
            
            if previous_value is not None:
                deficit = previous_value - value
                if deficit > 0:  # Only consider positive deficits
                    deficit_result.append((day, deficit))
            
            previous_value = value
        
        return deficit_result

    deficit_list = calculate_deficit(pl)

    for entry in deficit_list:
        day = entry[0]
        deficit = entry[1]
        deficit_str = f"[PROFIT DEFICIT] Day: {day}, AMOUNT: USD{deficit}\n"
        result += deficit_str

# Write the results to a file
fp_write = Path.cwd() / "summary_report.txt"
fp_write.touch()

with fp_write.open(mode="w", encoding="UTF-8") as file:
    file.write(result)

# print(result)