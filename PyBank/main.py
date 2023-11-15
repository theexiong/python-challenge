import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    total = 0    
    average = 0
    row_count = 0
    pl = []
    dates = []
    changes = []
    previous_num = 0
    current_pl = 0
    difference = 0
    greatest_profit_increase = ""
    greatest_profit_loss = ""
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    #for loop
    for row in csvreader:
        #count how many rows
        row_count += 1
        #add each row to total rows count
        total += int(row[1])

        #add pl values in each row to pl list
        pl.append(int(row[1]))

        #find difference between two values (ex: 2 - 1)
        difference = int(row[1]) - previous_num
        #add pl difference date values to dates list
        dates.append(row[0])
        #add pl difference values to changes list
        changes.append(difference)
        #set previous_num to current row value
        previous_num = int(row[1])
        #reset difference back to 0
        difference = 0

    #calculate average of first value and last value
    average = (pl[-1] - pl[0]) / (row_count - 1)
    #set greatest_profit to largest number in changes list
    greatest_profit = max(changes)
    #set greatest_loss to smallest number in changes list
    greatest_loss = min(changes)
    #find greatest profit increase by calling date that is associated with greatest profit value in changes list
    greatest_profit_increase = dates[changes.index(greatest_profit)]
    #find greatest profit loss by calling date that is associated with greatest loss value in changes list
    greatest_profit_loss = dates[changes.index(greatest_loss)]

#analysis variable for all information as f string
analysis = (f'''Financial Analysis\n
------------------------------\n
Total Months: {row_count}\n
Total: ${total}\n
Average Change: ${average:.2f}\n
Greatest Increase in Profits: {greatest_profit_increase} ${greatest_profit}\n
Greatest Decrease in Profits: {greatest_profit_loss} ${greatest_loss}''')

print(analysis)

#create output file
output_file = os.path.join ('Analysis', "Financial_Analysis.txt")

#open txt file and print analysis variable
with open(output_file, "w", newline = '') as datafile:
    writer = csv.writer(datafile)
    print(analysis, file=datafile)






