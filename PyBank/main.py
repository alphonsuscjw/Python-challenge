
# Module for reading CSV files
import csv

# Function to calculate the average change over the whole period in a dataset
def avg_change(initial, final, num_change):
    length = num_change # num_change is the total number of changes
    total_change = final - initial
    return total_change / length

# Function to calculate the greatest change in values in a dataset
def greatest_change(ini_list, final_list, ini_change):
    greatest_change = ini_change # ini_change is used to initialise the greatest_change variable
    change = int(final_list[1]) - int(ini_list[1])
    
    # Compare the absolute values of the change between 2 input values and the greatest change so far
    # Absolute values are taken so as to allow this function to be used for finding the greatest decrease as well
    if abs(change) > abs(greatest_change[1]):
        
        # If the change between the 2 input values is greater than the initial greatest_change, set it to be the greatest change
        greatest_change[1] = change

        # Record the corresponding date of the greatest change
        greatest_change[0] = final_list[0]

    return greatest_change

csv_path = 'C:/Users/User/Documents/Data Analytics Bootcamp/02-Homework/03-Python/Python-challenge/PyBank/Resources/budget_data.csv'

# Open the budget_data.csv file
with open(csv_path, encoding='utf') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header and append it to a list called "rows"
    rows = [row for row in csvreader]

# A budgetdata dict that contains the variables for the values to be output
budgetdata = {"total_months": 0, # the total number of months included in the dataset
    "total_prof_loss": 0, # the net total amount of "Profit/Losses" over the entire period
    "average_change": 0, # the average change in "Profit/Losses" over the entire period
    "greatest_prof_inc": ["date",0], # the greatest increase in profits (date and amount) over the entire period
    "greatest_prof_dec": ["date",0] # the greatest decrease in profits (date and amount) over the entire period
}

# The total number of months is simply the total number of data rows after the header in the csv file since no date is repeated
budgetdata["total_months"] = len(rows)

# Iterate through the data set
for i in range(len(rows)):
    
    # the net total amount of "Profit/Losses" over the entire period is simply the total sum of profit/losses over the entire period
    budgetdata["total_prof_loss"] += int(rows[i][1])
    
    # Calculate the greatest increase and the greatest decrese in profit
    if (i+1) < len(rows): # This if statement makes sure the iteration stays within the bound of the data set
        
        # If the profit/loss value of this row is less than that of next row...
        if rows[i][1] < rows[i+1][1]:
            # Execute the greatest_change function to find the greatest increase in profit
            budgetdata["greatest_prof_inc"] = greatest_change(rows[i],rows[i+1],budgetdata["greatest_prof_inc"])
        
        # If the profit/loss value of this row is greater than that of next row...
        else:
            # Execute the greatest_change function to find the greatest decrease in profit
            budgetdata["greatest_prof_dec"] = greatest_change(rows[i],rows[i+1],budgetdata["greatest_prof_dec"])

# Calculate the average change in profit/loss over the whole period
budgetdata["average_change"] = round(avg_change(float(rows[0][1]), float(rows[len(rows)-1][1]), budgetdata["total_months"]-1),2)

# List to hold the lines to be output
output_list = [
    "\nFinancial Analysis\n",
    "-------------------------------\n",
    f'Total Months: {budgetdata["total_months"]}\n',
    f'Total: ${budgetdata["total_prof_loss"]}\n',
    f'Average Change: ${budgetdata["average_change"]}\n',
    f'Greatest Increase in Profits: {budgetdata["greatest_prof_inc"][0]} (${budgetdata["greatest_prof_inc"][1]})\n',
    f'Greatest Decrease in Profits: {budgetdata["greatest_prof_dec"][0]} (${budgetdata["greatest_prof_dec"][1]})\n'
]

# Print the output results on the terminal
for i in output_list:
    print(i)

# Specify the text file to write to
output_path = 'C:/Users/User/Documents/Data Analytics Bootcamp/02-Homework/03-Python/Python-challenge/PyBank/Analysis/PyBank.txt'

# Open the text file using "write" mode
with open(output_path, 'w') as f:

    # Write the output results to the text file
    for i in output_list:
        f.write(i + "\n") # Function learned from https://www.pythontutorial.net/python-basics/python-write-text-file/#:~:text=To%20write%20to%20a%20text,using%20the%20close()%20method