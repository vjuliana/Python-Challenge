# Create a script that analyses the records to calculate
## total no. of months in the dataset 
## net total amount of "Profit/Losses" over the entire period 
## the average of the changes in "Profit/Losses" over the entire period
## the greatest increase in profit (date and amount) over the entire period 
## the greatest decrease in losses (date and amount) over the entire period 

## EXAMPLE
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# -------------------------------------------------------------------------

# Import modules to read csv
import os
import csv

# Join path to csv file 'budget_data'
csvpath = os.path.join('PyBank', 'Resources' , 'budget_data.csv')

# Read file
with open(csvpath, 'r') as csvfile:
    bank_data = csv.reader(csvfile, delimiter=',')
    
     # Read the header row first 
    csv_header = next(bank_data)
    print(f"Header: {csv_header}")


# Each row is read as a row
    for row in bank_data:
        print(row)
