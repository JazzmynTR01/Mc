## profit_loss.py
## will be used as a module

## import required modules
from pathlib import Path
import csv

def pl_func():
    """
    This function will compute whether the profit daily is always increasing or not 
    if yes, it will find the surplus 
    if not, it will find the days where the current day value is less than the previous day 
    """

    # find the csv file from the csv_report folder
    fp_read = Path.cwd()/"csv_reports"/"profit and loss.csv"
    # create a file to write into the summary report
    fp_write = Path.cwd()/"summary_report.txt"

    # read the csv file 
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        # using .reader(), read the cash on hand csv file
        reader = csv.reader(file)
        next(reader) # skip header

        # create empty lists to store data
        pl = []
        
        for row in reader:
            # append the organzised data into the new list
            pl.append([row[0],row[4]])


    def is_list_increasing(lst):
        """
        This function check if data is always higher than the previous day
        """
        for i in range(1, len(lst)):
            # Loop through the list starting from the second element
            if lst[i] <= lst[i-1]:
                # Compare the current element with the previous element
                # If the current element is less than or equal to the previous element, the data is not increasing
                return False
        return True

    # If cash is always higher than the previous day, the code will give the cash surplus
    if is_list_increasing(pl):
        # using if to identify if net profit is lesser than the previous day
        result = "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        
        def calculate_highest_surplus(data):
            """
            This function will calculate the surplus if the 
            data is always increasing
            """
            highest_surplus = 0 # Used to keep track of the highest surplus amount encountered so far
            previous_value = None # To store the value from the previous day in the loop
            day_with_highest_surplus = None # To store the day with the highest surplus encountered so far
            
            for entry in data:
                day = entry[0]
                value = float(entry[1]) # Extract and convert to float
                
                if previous_value is not None: # Check if there's a valid previous_value 
                    # if condition applies, use operators to compute the difference of the identified days and assign them to surplus
                    surplus = value - previous_value

                    if surplus > highest_surplus: # Check if the calculated surplus is greater than the current highest_surplus

                        highest_surplus = surplus # Update highest_surplus with the new surplus
                        day_with_highest_surplus = day # Update day_with_highest_surplus with the current day
            
                previous_value = value  # Update previous_value for the next iteration with the current value

            # Return the day with the highest surplus and the value of the highest surplus
            return day_with_highest_surplus, highest_surplus
        
        day, highest_surplus = calculate_highest_surplus(pl)
        # open the text summary txt 
        with fp_write.open(mode="a", encoding="UTF-8", newline="" ) as file:
            
            result += f"[HIGHEST NET PROFIT SURPLUS] DAY {day}, AMOUNT: USD{highest_surplus:.0f}\n"
            file.write(result) # write the results into the txt file

    # This function will then calculate and store the deficits
    else:
        result = ""
        
        def calculate_deficit(data):
            """
            This function will calculate the deficits if data is not always increasing
            """
            previous_value = None  # Initialize the previous_value to None
            deficit_result = [] # Create an empty list to store deficit data
            
            for entry in data:
                day = int(entry[0]) # Extract and convert to interger
                value = int(entry[1]) # Extract and convert to interger
                
                if previous_value is not None: # Check if there's a valid previous_value 
                    # if condition applies, use operators to compute the difference of the identified days and assign to deficit
                    deficit = previous_value - value
                    if deficit > 0:  # Only consider positive deficits
                        deficit_result.append((day, deficit)) # Append the day and deficit to deficit_result list
                
                previous_value = value # Update previous_value for the next iteration with the current value

            # Return the list containing tuples of days and their corresponding positive deficits
            return deficit_result

        deficit_list = calculate_deficit(pl)

        with fp_write.open(mode="a", encoding="UTF-8", newline="" ) as file:
            for entry in deficit_list:
                day = entry[0]
                deficit = entry[1]
                deficit_str = f"[PROFIT DEFICIT] Day: {day}, AMOUNT: USD{deficit}\n"
                result += deficit_str # Append the formatted string to the 'result' variable

            file.write(result) # write the results into the txt file
