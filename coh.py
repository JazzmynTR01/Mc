## coh.py
## will be used as a module

## import required modules
from pathlib import Path
import csv

fp_read = Path.cwd()/"csv_reports"/"coh.csv"
# print(fp_read.exists())

with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
    # using .reader(), read the cash on hand csv file
    reader = csv.reader(file)
    next(reader) # skip header

    # create empty lists to store data
    hand = []
    
    for row in reader:
        # append the data into the new list
        hand.append([row[0],row[1]]) 


def is_list_increasing(list):
        """
        This function check if data is always higher than the previous day
        """
        for i in range(1, len(list)):
            # Loop through the list starting from the second element
            if list[i] <= list[i-1]:
            # Compare the current element with the previous element
            # If the current element is less than or equal to the previous element, the data is not increasing
                return False
        return True

if is_list_increasing(hand):
    # Print to say that it is a surplus 
    result = "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"

    def calculate_highest_surplus(data):
        """
        This function will calculate the surplus if the 
        data is always increasing
        """
        # Initialize variables to track the highest surplus and associated day
        highest_surplus = 0
        previous_value = None
        day_with_highest_surplus = None
       
       # Loop through each entry in the data list 
        for entry in data:

            day = entry[0] # Extract day from the entry
            value = float(entry[1]) # Extract value from the entry
            
            if previous_value is not None:
                # if condition applies use operators to compute the difference and assign them to surplus
                surplus = value - previous_value

                # Check if the current surplus is higher than the highest recorded surplus
                if surplus > highest_surplus:
                    highest_surplus = surplus
                    day_with_highest_surplus = day # Update the day with the highest surplus
            
            previous_value = value  # Update the previous value for the next iteration
        
         # Return the day and the highest surplus found
        return day_with_highest_surplus, highest_surplus
    
    day, highest_surplus = calculate_highest_surplus(hand)
    result += f"[HIGHEST CASH SURPLUS] DAY {day}, AMOUNT: USD{highest_surplus:.0f}\n"

else:
    result = ""

    def calculate_deficit(data):
        """
        This function will calculate the deficits if data is not always increasing
        """
        previous_value = None
        result_def = [] # Create an empty list to store deficit entries
        
        for entry in data:

            day = entry[0] # Extract day from the entry
            value = float(entry[1]) # Extract value from the entry
            
            if previous_value is not None:
                # if condition applies, use operators to compute the difference of the identified days and assign to deficit
                deficit = previous_value - value
                if deficit > 0:  # Only consider positive deficits
                    result_def.append((day, deficit)) # Add day and deficit to the list
            
            previous_value = value # Update the previous value for the next iteration
        
        return result_def # Return the list of deficit entries
    
    deficit_list = calculate_deficit(hand)  # Calculate deficits using the provided data

    for entry in deficit_list:
        day = entry[0]
        deficit = entry[1]
        deficit_str = f"[CASH DEFICIT] Day: {day}, AMOUNT: USD{deficit:.0f}\n"
        result += deficit_str # Concatenate deficit information to the result string

