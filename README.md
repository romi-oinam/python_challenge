# python_challenge

#Bybank assignment

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

#____________________________________________________________________________________________________________


#Bypoll assignment

#Import csv file.

import csv
import os

#Path for Resources Data.

election_data_path = os.path.join("Resources","election_data.csv")
output_path = os.path.join("Analysis", "election_analysis_output.txt")

#Empty List

voterids = []
counties = []
candidates = []
candidatenames = []
totalvotesforcandidate = []
resultprintcandidate = []
totalpercentagevotesforcandidate = []

#Start conditions.

Total_votes = 0
winnervotes = 0
loservotes = 0
loop1 = 0
loop2 = 0
loop3 = 0
loop4 = 0

#Open in read mode and skip to Header

with open(election_data_path, 'r') as f:
    election_reader = csv.reader(f, delimiter=',')
    election_header = next(election_reader)

#Filling up the empty list

    for row in election_reader:
        voterid = row[0]
        county = row[1]
        candidate = row[2]
        voterids.append(voterid)
        counties.append(county)
        candidates.append(candidate)

#The total number of vots cast in the "Voter ID" column.

    Total_votes = len(voterids)

#Pre_load first candidate name for comparision.

candidatenames.append(candidates[0])

#First Loop is through the list of candidates to determine candidates voted for (variable loop1 as loop index counter).

for loop1 in range (Total_votes-1):
        if candidates[loop1 + 1] != candidates[loop1] and candidates[loop1+1] not in candidatenames:
             candidatenames.append(candidates[loop1 + 1])

n = len(candidatenames)

#Second loop variable loop2 as loop index counter.

#Range of loop depending on how many candidates were found, then count total votes of candidates & add to list total.
for loop2 in range (n):
        totalvotesforcandidate.append(candidates.count(candidatenames[loop2]))

# Third loop variable loop3 as loop index counter

#Pre-lood loservoters with maximum votes for < comparision.

loservotes = Total_votes

#Range of loop depending on ow many candidates were found, then calculate % votes per candidate found.

for loop3 in range(n):
        totalpercentagevotesforcandidate.append(f"{round((totalvotesforcandidate[loop3]/Total_votes*100), 3)}%")

        if totalvotesforcandidate[loop3]> winnervotes:
            winner = candidatenames[loop3]
            winnervotes = totalvotesforcandidate[loop3] #candidate with highest vote count.

       
#Fouth loop variable loop4 as loop index counter

for loop4 in range(n):
        resultprintcandidate.append(f"{candidatenames[loop4]}: {totalpercentagevotesforcandidate[loop4]} ({totalvotesforcandidate[loop4]})")

resultlines = '\n'.join(resultprintcandidate)


#Print the Output and Save the text file.

print(f'Election Results')
print(f'------------------------------------')
print(f'Total Votes: {Total_votes}')
print(f'------------------------------------')
print(resultlines)
print(f'------------------------------------')
print(f'Winner : {winner}')
print(f'------------------------------------')

with open(output_path, 'w') as text:
      text.write("Election Results\n")
      text.write(f'------------------------------------\n')
      text.write(f'Total Votes: {Total_votes}\n')
      text.write(f'------------------------------------\n')
      text.write(f'{resultlines}\n')
      text.write(f'------------------------------------\n')
      text.write(f'Winner : {winner}\n')
      text.write(f'------------------------------------\n')