# Import the csv
import os
import csv
budget_data_csv = os.path.join("Resources", "election_data.csv")

# Define Variables
all_votes = 0
unique_candidates = []
candidate_totalvote = []

# Open File in Python 
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    # For loop to look through data
    for row in csvreader:
        
        #This is the total votes cast, and all canidate names
        all_votes += 1
        candidates = (row[2])
        
        #for all canidates, increase their vote count by 1 
        if candidates in unique_candidates:
            candidate_index = unique_candidates.index(candidates)
            candidate_totalvote[candidate_index] = candidate_totalvote[candidate_index] + 1
        else:
            #add all the unique votes to unique_candiates list
            unique_candidates.append(candidates)
            candidate_totalvote.append(1)

# Define Variables
percent = []
most_votes = candidate_totalvote[0]
most_index = 0

# For loop to look through data
for x in range(len(unique_candidates)):
    vote_percent = round(candidate_totalvote[x]/all_votes*100, 2)
    percent.append(vote_percent)
    
    
    if candidate_totalvote[x] > most_votes:
        most_votes = candidate_totalvote[x]
        most_index = x

election_winner = unique_candidates[most_index] 

#Print Election Results 
print(f'Election Results')
print('----------------------------------------')
print(f'Total Votes: {all_votes}')
print('----------------------------------------')
for x in range(len(unique_candidates)):
    print(f'{unique_candidates[x]} : {percent[x]}% ({candidate_totalvote[x]})')
print('----------------------------------------')
print(f'Election winner: {election_winner}')

outputfile = open("Election Results.txt", "w")
outputfile.write(f'Election Results')
outputfile.write("\n")
outputfile.write(f'-----------------------------------')
outputfile.write("\n")
outputfile.write(f'Total Votes: {all_votes}')
outputfile.write("\n")
outputfile.write(f'-----------------------------------')
outputfile.write("\n")
for x in range(len(unique_candidates)):
    outputfile.write(f'{unique_candidates[x]} : {percent[x]}% ({candidate_totalvote[x]})')
    outputfile.write("\n")
outputfile.write(f'-----------------------------------')
outputfile.write("\n")
outputfile.write(f'Election winner: {election_winner}')
outputfile.close()