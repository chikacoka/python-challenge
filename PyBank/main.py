# Import the os module as this will enable us to create file paths across operating systems
#Import module for reading CSV files

import os
import csv

# Set path for file

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Define Variables
month_count = 0
net_total_amount_of_profit = 0
total_profit_loss_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
profit_loss = 0
net_change_list = []
all_months = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    first_row = next(csvreader)
    month_count += 1
    profit_loss += int(first_row[1])
    previous_profit_loss = int(first_row[1])

    # Loop through each row of data after the header
    for row in csvreader:
        month_count += 1
        profit_loss += int(row[1])
        current_profit_loss = int(row[1]) - previous_profit_loss
        previous_profit_loss = int(row[1])
        net_change_list += [current_profit_loss]
        total_profit_loss_change += [row[0]]
        change_in_profit_loss = current_profit_loss - previous_profit_loss
        all_months.append(row[0])


net_monthly_average = round(sum(net_change_list)/len(net_change_list), 2)
greatest_increase = max(net_change_list)
greatest_decrease = min(net_change_list)

x = net_change_list.index(max(net_change_list))
a = net_change_list.index(min(net_change_list))

y = all_months[x]
b = all_months[a]

#print("x=", x)
# print("y=", y)
#print("a=", a)
#print("b=", b)

# Print the analysis to the terminal and also export as text file to the Analysis folder

print(f"Financial Analysis")
print("--------------------------------")
print(f"Total Months: {str(month_count)}")
print(f"Total Net Profit: ${str(profit_loss)}")
print(f"Average Change: ${str(net_monthly_average)}")
print(f"Greatest Increase in Profits: {y} ${str(greatest_increase)}")
print(f"Greatest Decrease in Profits: {b} ${str(greatest_decrease)}")


output_file = os.path.join("Analysis", "budget_data copy.text")
with open(output_file, "w",) as text:
    text.write(f"Financial Analysis\n")
    text.write(f"--------------------------------\n")
    text.write(f"Total Months: {str(month_count)}\n")
    text.write(f"Total Net Profit: ${str(profit_loss)}\n")
    text.write(f"Average Change: ${str(net_monthly_average)}\n")
    text.write(
        f"Greatest Increase in Profits: {y} ${str(greatest_increase)}\n")
    text.write(
        f"Greatest Decrease in Profits: {b} ${str(greatest_decrease)}\n")
