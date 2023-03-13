#Import csv file.

import csv
import os

#Path for Resources Data.

budgetpath = os.path.join("Resources","budget_data.csv")
output_path = os.path.join("Analysis", "analysis_output.txt")

#Empty List

Months = []
Amount = []
Difference = []
Prev = 0

#Open in read mode and skip to Header

with open(budgetpath, 'r') as f:
    budget_reader = csv.reader(f, delimiter=',')
    budget_header = next(budget_reader)

#Filling up the empty list

    for row in budget_reader:
        Months.append(row[0])
        Amount.append(row[1])

#Finding Difference & make a list.
        x = int(row[1]) - int(Prev)
        Prev = row[1]
        Difference.append(x)

#Using the zip function for parallel iteration.

clean = zip(Months, Difference)
clean_lst = list(clean)
Difference.remove(Difference[0])
clean_lst.remove(clean_lst[0])

#Calculating Total, Avgerage, Greatest Increase in Profit & Great Decrease in Profit.

total = sum(map(int, Amount))
average_change = sum(Difference) / len(Difference)
increase = max(Difference)
decrease = min(Difference)
Greatest_Increase = 0
Greatest_Decrease = 0
for row in clean_lst:
    if row[1] == increase:
        Greatest_Increase = row[0]
    if row[1] == decrease:
        Greatest_Decrease = row[0]

#Print the Output and Save the text file.

print(f'Financial Analysis')
print(f'------------------------------------')
print(f'Total Months: {len(Amount)}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {Greatest_Increase} (${increase})')
print(f'Greatest Decrease in Profits: {Greatest_Decrease} (${decrease})')
with open(output_path, 'w') as text:
      text.write("Financial Analysis\n")
      text.write(f'------------------------------------\n')
      text.write(f'Total Votes: {len(Amount)}\n')
      text.write(f'Total: ${total}\n')
      text.write(f'Average Change: ${average_change:.2f}\n')
      text.write(f'Greatest Increase in Profits: {Greatest_Increase} (${increase})\n')
      text.write(f'Greatest Increase in Profits: {Greatest_Decrease} (${decrease})\n')