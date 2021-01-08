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

# Track various financial parameters
total_months = 0 # starting number
total_net = 0 # starting number
net_change_list = [] # to track average change
greatest_increase = [" ", 0] # format of greatest increase
greatest_decrease = [" ", 9999999999999999999] # format of greatest decrease


# Read file as a csvfile
with open(csvpath, 'r') as csvfile:
    bank_data = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first 
    csv_header = next(bank_data)
    # print(f"Header: {csv_header}")

    # To read rows thereafter 
    first_row = next(bank_data) 
    total_months += 1 
    total_net += int(first_row[1]) # adding values in second column of first row
    prev_net = int(first_row[1]) #specifying that the previous value is an integer from the second column of the first row

# Each row is read as a row
    for row in bank_data:
        total_months += 1 # adding one for every row the loop goes through - only for total months
        total_net += int(row[1]) # adding the value in the profit/loss column every time the loop goes through the row
        
        # Track the change month-to-month
        net_change = int(row[1]) - prev_net # calculating the changes month-to-month
        prev_net = int(row[1]) # defined again that the previous value is an integer from the second column of the first row
        net_change_list += [net_change] # storing all the observations in the list

        # Greatest increase 
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0] # date-month
            greatest_increase[1] = net_change # amount

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0] # date-month
            greatest_decrease[1] = net_change # amount

# Not-to-self: VS Code reads it by row, and not by columns  

# Printing results

print("FINANCIAL ANALYSIS")
print("----------------------------")

# Total month
print("Total months :", total_months)

# Total profit/loss
print("Total : $", total_net)

# Average net change
net_change_average = sum(net_change_list) / len(net_change_list)
print("Average change: $", round(net_change_average,2))

# Greatest increase & decrease
print(f"Greatest increase: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest decrease: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write and export prints to text file 
analysis = open("Analysis_Pybank.txt", "w")

print(f"FINANCIAL ANALYSIS", file = analysis)
print(f"----------------------------", file = analysis)
print(f"Total months : {total_months}", file = analysis)
print(f"Total : $ {total_net}", file = analysis)
print(f"Average change: $ {round(net_change_average,2)}", file = analysis)
print(f"Greatest increase: {greatest_increase[0]} (${greatest_increase[1]})", file = analysis)
print(f"Greatest decrease: {greatest_decrease[0]} (${greatest_decrease[1]})", file = analysis)