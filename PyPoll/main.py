import os
import csv

# File paths
input_csv = os.path.join("Resources", "election_data.csv")
output_folder = "Analysis"
output_txt = os.path.join(output_folder, "election_results.txt")

# Lists to store data
Total_Votes = []
Candidates = []

# Dictionary to store the number of votes for each candidate
Votes_Per_Candidate = {}

# Open the CSV file
with open(input_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Add vote to Total_Votes list
        Total_Votes.append(row[0])

        # Add candidate to Candidates list
        Candidates.append(row[2])

# Calculate the total number of votes cast
total_votes_cast = len(Total_Votes)

# Calculate the total number of votes each candidate won
for candidate in Candidates:
    Votes_Per_Candidate[candidate] = Votes_Per_Candidate.get(candidate, 0) + 1

# Calculate the percentage of votes each candidate won
percentage_per_candidate = {candidate: (votes / total_votes_cast) * 100 for candidate, votes in Votes_Per_Candidate.items()}

# Find the winner of the election based on the highest number of votes
winner = max(Votes_Per_Candidate, key=Votes_Per_Candidate.get)

# Ensure the "Analysis" folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Export the analysis to a text file in the "Analysis" folder
with open(output_txt, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes_cast}\n")
    output_file.write("-------------------------\n")

    # Write a complete list of candidates who received votes
    for candidate, votes in Votes_Per_Candidate.items():
        output_file.write(f"{candidate}: {percentage_per_candidate[candidate]:.3f}% ({votes})\n")

    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

# Print a message indicating the export
print(f"Results exported to '{output_txt}'.")
