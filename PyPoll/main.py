# Create a script to modernize vote counting process. 
# The 'election_data.csv' composed of three columns: 
#     Voter ID, 
#     County, and 
#     Candidate. 

# Create a script to calculate each of the following:
#     The total number of votes cast
#     A complete list of candidates who received votes
#     The percentage of votes each candidate won
#     The total number of votes each candidate won

# The winner of the election based on popular vote.

# EXAMPLE
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

# In addition, your final script should both print the analysis to the terminal and export a text file with the results

# -------------------------------------------------------------------------

# Import modules to read csv
import os
import csv

# Join path to csv file 'budget_data'
csvpath = os.path.join('PyPoll', 'Resources' , 'election_data.csv')

# Track various parameters
total_votes = 0 # starting number for total votes 
candidate_list = {} # dictionary for candidate names and tally of votes
votes_stats = {} # dictionary for the % of total votes per candidate
vote_percent = []
winner = []
winner_tally = 0 # for the greatest number of votes received

# Read file as a csvfile
with open(csvpath) as csvfile:
    election_results = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(election_results)
    # print(f"Header: {csv_header}")

    # To read rows thereafter 
    first_row = next(election_results) 

    # Each row is read as a row
    for row in election_results:
        total_votes += 1 # adding one for every row the loop goes through to find the total number of votes casted
        
        # Track the candidates
        candidate_names = row[2] # variable name
        candidate_votes = 0 # starting number

        # if statements:
            # if candidate is in dictionary, keep adding 1 to the votes counter 
            # if the candidate is not in the dictionary, add name to the dictionary and the number of time the candidate appears
        
        if candidate_names in candidate_list.keys():
            candidate_list[row[2]] += 1

        if candidate_names not in candidate_list.keys():
            candidate_list[row[2]] = 1
    
    # First find the candidate with the most votes
    winner_tally = max(candidate_list.values())
    # print(winner_tally)
    # print(candidate_list.values())

    # Calculate the % of votes for each candidate using .items()
    for names, votes in candidate_list.items():
        if names not in votes_stats: 
            votes_stats[0] = [names]
            votes_stats[1] = round(((votes / total_votes)*100),3)

        if winner_tally == votes:
            winner = names

# Write and export prints to text file 
# Create text file 
analysis = open("Analysis_PyPoll.txt", "w")

print(f"Election Results", file = analysis)
print(f"-------------------------", file = analysis)
print(f"Total votes: {total_votes}", file = analysis)
print(f"-------------------------", file = analysis)
for names, votes in candidate_list.items():           
    print("{} :" f" {votes_stats[1]}.00%" " ({})".format(names, votes), file = analysis)
print(f"-------------------------", file = analysis)
print(f"Winner : {winner}", file = analysis)
print(f"-------------------------", file = analysis)
