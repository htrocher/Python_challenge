# import dependencies

import pandas as pd
import sys

# set the file for text output instead of console

sys.stdout = open('/Users/hugotroche/GitHub/Python_challenge/PY_Poll/Analysis_P/Analysis_P_R1.txt',"w")


# Load the dataset
file_path = '/Users/hugotroche/GitHub/Python_challenge/PY_Poll/Resources_P/election_data.csv'
df = pd.read_csv(file_path)

# 1) Total number of votes cast from "Ballot ID"
total_votes = len(df['Ballot ID'])

# 2) Complete list of candidates who received votes from "Candidate"
candidates_list = df['Candidate'].unique()

# 3) Percentage of votes each candidate won from "Candidate"
percentage_votes = df['Candidate'].value_counts(normalize=True) * 100

# 4) Total number of votes each candidate won from "Candidate"
total_votes_per_candidate = df['Candidate'].value_counts()

# 5) Winner of the election based on popular vote from "Candidate"
winner = total_votes_per_candidate.idxmax()

# Print the results
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print("Candidates who received votes:")
for candidate in candidates_list:
    print(f"{candidate}: {percentage_votes[candidate]:.3f}% ({total_votes_per_candidate[candidate]})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")
