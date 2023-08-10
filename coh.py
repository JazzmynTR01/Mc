## coh.py
## will be used as a module

## import required modules
from pathlib import Path
import csv


def coh_func():
    """
    This function will compute whether the cash on hand daily is always increasing or not 
    if yes, it will find the surplus 
    if not, it will find the days where the current day value is less than the previous day 
    """
    # find the csv file from the csv_report folder
    fp_read = Path.cwd()/"csv_reports"/"coh.csv"
    # create a file to write into the summary report
    fp_write = Path.cwd()/"summary_report.txt"

    # open the csv file
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        # using .reader(), read the cash on hand csv file
        reader = csv.reader(file)
        next(reader) # skip header

        # create empty lists to store data
        hand = []
        
        for row in reader:
            # append the organzised data into the new list
            hand.append([row[0],row[1]]) 


    def is_list_increasing(hand):
            """
            This function check if data is always higher than the previous day
            """
            for i in range(1, len(hand)):
                # Loop through the list starting from the second element
                if hand[i] <= hand[i-1]:
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
            previous_day = None
            day_with_highest_surplus = None
        
        # Loop through each entry in the data list 
            for entry in data:

                day = entry[0] # Extract day from the entry
                value = float(entry[1]) # Extract value from the entry
                
                if previous_day is not None:
                    # if condition applies use operators to compute the difference and assign them to surplus
                    surplus = value - previous_day

                    # Check if the current surplus is higher than the highest recorded surplus
                    if surplus > highest_surplus:
                        highest_surplus = surplus
                        day_with_highest_surplus = day # Update the day with the highest surplus
                
                previous_day = value  # Update the previous value for the next iteration
            
            # Return the day and the highest surplus found
            return day_with_highest_surplus, highest_surplus
        day, highest_surplus = calculate_highest_surplus(hand)
        
        # open the txt file 
        with fp_write.open(mode="a", encoding="UTF-8", newline="" ) as file:
            result += f"[HIGHEST CASH SURPLUS] DAY {day}, AMOUNT: USD{highest_surplus:.0f}\n"

            file.write(result) # write the results into the txt file

    else:
        result = ""

        def calculate_deficit(data):
            """
            This function will calculate the deficits if data is not always increasing
            """
            previous_day = None
            result_def = [] # Create an empty list to store deficit entries
            
            for entry in data:

                day = entry[0] # Extract day from the entry
                value = float(entry[1]) # Extract value from the entry
                
                if previous_day is not None:
                    # if condition applies, use operators to compute the difference of the identified days and assign to deficit
                    deficit = previous_day - value
                    if deficit > 0:  # Only consider positive deficits
                        result_def.append((day, deficit)) # Add day and deficit to the list
                
                previous_day = value # Update the previous value for the next iteration
            
            return result_def # Return the list of deficit entries
        
        deficit_list = calculate_deficit(hand)  # Calculate deficits using the provided data
        # open the txt file 
        with fp_write.open(mode="a", encoding="UTF-8", newline="" ) as file:

            for entry in deficit_list:
                day = entry[0]
                deficit = entry[1]
                deficit_str = f"[CASH DEFICIT] Day: {day}, AMOUNT: USD{deficit:.0f}\n"
                result += deficit_str # Concatenate deficit information to the result string

            file.write(result) # write the results into the txt file
