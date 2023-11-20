import pandas as pd

# Load the dataset
file_path = '/Users/hugotroche/Desktop/Bootcamp/Challenges/Challenge 3 /Poll_1/Resources/election_data.csv'
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
