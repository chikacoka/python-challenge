# Import the os module as this will enable us to create file paths across operating systems
#Import module for reading CSV files

import os
import csv

# Set the path for the file

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Define Variables

total_votes_cast = 0
all_candidates = []
county_names = []
candidate1_count = 0
candidate2_count = 0
candidate3_count = 0


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and the variable that holds the csv contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Loop through each row for each election data after the header

    for row in csvreader:
        total_votes_cast += 1
        candidate_name = row[2]
        county_name = row[1]

        if candidate_name not in all_candidates:
            all_candidates.append(candidate_name)
        if county_name not in county_names:
            county_names.append(county_name)
        candidate1 = str('Charles Casper Stockham')
        candidate2 = str('Diana DeGette')
        candidate3 = str('Raymon Anthony Doane')
        if candidate1 in candidate_name:
            candidate1_count += 1
        if candidate2 in candidate_name:
            candidate2_count += 1
        if candidate3 in candidate_name:
            candidate3_count += 1

    # Calculate each candidate's percentage of votes received out of total vote cast
percentage_vote_candidate1 = (candidate1_count / total_votes_cast) * 100
percentage_vote_candidate2 = (candidate2_count / total_votes_cast) * 100
percentage_vote_candidate3 = (candidate3_count / total_votes_cast) * 100
max_votes_count = max(candidate1_count, candidate2_count, candidate3_count)

    # Create conditional statements to establish the winning candidate based on maximum votes received
if max_votes_count == candidate1_count:
    winner = candidate1
elif max_votes_count == candidate2_count:
    winner = candidate2
else:
    winner = candidate3

# Print the analysis to the terminal and also export as text file to the Analysis folder

print(f"Election Results")
print("--------------------------------")
print(f"Total Votes: {str(total_votes_cast)}")
print("--------------------------------")
print(
    f"Charles Casper Stockham: {round(percentage_vote_candidate1,3)}% ({int(candidate1_count)})")
print(
    f"Diana DeGette:  {round(percentage_vote_candidate2,3)}% ({int(candidate2_count)})")
print(
    f"Raymon Anthony Doane:  {round(percentage_vote_candidate3,3)}% ({int(candidate3_count)})")
print("--------------------------------")
print(f"winner: {winner}")
print("--------------------------------")

output_file = os.path.join("Analysis", "election_data copy.text")
with open(output_file, "w",) as text:

    text.write(f"Election Results\n")
    text.write(f"--------------------------------\n")
    text.write(f"Total Votes: {str(total_votes_cast)}\n")
    text.write("--------------------------------\n")
    text.write(
        f"Charles Casper Stockham: {round(percentage_vote_candidate1,3)}% ({int(candidate1_count)})\n")
    text.write(
        f"Diana DeGette: {round(percentage_vote_candidate2,3)}% ({int(candidate2_count)})\n")
    text.write(
        f"Raymon Anthony Doane: {round(percentage_vote_candidate3,3)}% ({int(candidate3_count)})\n")
    text.write("--------------------------------\n")
    text.write(f"winner: {winner}\n")
    text.write("--------------------------------\n")
