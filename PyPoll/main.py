
# Module for reading CSV files
import csv

csv_path = 'C:/Users/User/Documents/Data Analytics Bootcamp/02-Homework/03-Python/Python-challenge/PyPoll/Resources/election_data.csv'

# Open the election_data.csv file
with open(csv_path, encoding='utf') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header and append it to a list called "rows"
    rows = [row for row in csvreader]

# Function to extract from the data set the complete list of candidates who received votes
def candidates(data_rows):
    candidate_list = []

    # Iterate through the input data set
    for i in range(len(data_rows)):
        if (i+1) < len(data_rows): # This if statement makes sure the iteration stays within the bound of the data set
            
            # If the candidate name in this row is different from that in the next row...
            if data_rows[i][2] != data_rows[i+1][2]:
                
                # and if the candidate name in this row is not already in the candidate_list...
                if all(data_rows[i][2] != j for j in candidate_list):
                    
                    # Append the name to the candidate_list
                    candidate_list.append(data_rows[i][2])
    
    return candidate_list

# Function to calculate the total number of votes won by each candidate
def votes_won(candidate_list, data_rows):
    votes_won = 0
    votes_won_list = []

    # Iterate through the input candidate list
    for j in candidate_list:
        
        # Iterate through the input data set
        for i in range(len(data_rows)):
            
            # If the candidate name in this row equals to the candidate name of this iteration in the candidate_list...
            if (data_rows[i][2] == j):
                
                # Add 1 vote won for the candidate
                votes_won += 1
        
        # Append the total votes won by the candidate of this iteration to the votes_won_list
        votes_won_list.append(votes_won)

        # Reset the vote count to 0 for use by the candidate of the next iteration
        votes_won = 0
    
    # This function is designed to align each total number of votes won in votes_won_list with the correct corresponding candidate in candidate_list
    # So the first element in votes_won_list corresponds with the first candidate in candidate_list, and so on
    return votes_won_list

# Function to calculate the percentage of votes won by each candidate
def percent_won(votes_won_list,total_votes):
    percent_won_list = []

    # Iterate through the input list for votes won 
    for j in votes_won_list:

        # The percentage of votes won by a candidate is simply, in percent form, the ratio of total number of votes won by a candidate to the total number of votes casted
        percent_won = round(j/total_votes*100,3)

        # Append the percentage of votes won in this iteration to the percent_won_list
        percent_won_list.append(percent_won)

    # This function is also designed to align each percentage of votes won in percent_won_list with the correct corresponding total number of votes won in votes_won_list
    # So the first element in percent_won_list corresponds with the first element in votes_won_list, and so on
    return percent_won_list

# Function to determine the winner among all candidates
def win(candidate_list,percent_won_list):

    # The winner is the one who receives the highest percentage of votes
    # Find the element with the highest percentage of votes
    winner_votes = max(percent_won_list)

    # Find the corresponding index number for that element
    winner_index = percent_won_list.index(winner_votes)

    # This index number is the same as that for the candidate in the input candidate_list, who is the winner
    return candidate_list[winner_index]

# An electiondata dict that contains the variables for the values to be output
electiondata = {"total_votes": 0, # The total number of votes cast
    "candidates": [], # The complete list of candidates who received votes
    "percent_won": [], # The percentage of votes each candidate won
    "votes_won": [], # The total number of votes each candidate won
    "winner": "" # The name of the winner of the election based on popular vote
}

# The total number of votes cast is simply the total number of data rows after the header in the csv file since no two ballots should have the same ID
electiondata["total_votes"] = len(rows)

# Extract from the data set the complete list of candidates who received votes
electiondata["candidates"] = candidates(rows)

# Calculate the total number of votes won by each candidate
# The first element in electiondata["votes_won"] corresponds with the first candidate in electiondata["candidates"], and so on
# See further explanation in votes_won function
electiondata["votes_won"] = votes_won(electiondata["candidates"],rows)

# Calculate the percentage of votes won by each candidate
# The first element in electiondata["percent_won"] corresponds with the first element in electiondata["votes_won"], which corresponds with the first candidate in electiondata["candidates"], and so on
# See further explanation in percent_won function
electiondata["percent_won"] = percent_won(electiondata["votes_won"],electiondata["total_votes"])

# Determine the winner among all candidates
winner = win(electiondata["candidates"],electiondata["percent_won"])

# List to hold the lines to be output
output_list = [
    "\nElection Results\n",
    "-------------------------------\n",
    f'Total Votes: {electiondata["total_votes"]}\n',
    "-------------------------------\n",
    f'{electiondata["candidates"][0]}: {electiondata["percent_won"][0]}% ({electiondata["votes_won"][0]})\n',
    f'{electiondata["candidates"][1]}: {electiondata["percent_won"][1]}% ({electiondata["votes_won"][1]})\n',
    f'{electiondata["candidates"][2]}: {electiondata["percent_won"][2]}% ({electiondata["votes_won"][2]})\n',
    "-------------------------------\n",
    f'Winner: {winner}\n',
    "-------------------------------\n"
]

# Print the output results on the terminal
for i in output_list:
    print(i)

# Specify the text file to write to
output_path = 'C:/Users/User/Documents/Data Analytics Bootcamp/02-Homework/03-Python/Python-challenge/PyPoll/Analysis/PyPoll.txt'

# Open the text file using "write" mode
with open(output_path, 'w') as f:

    # Write the output results to the text file
    for i in output_list:
        f.write(i + "\n") # Function learned from https://www.pythontutorial.net/python-basics/python-write-text-file/#:~:text=To%20write%20to%20a%20text,using%20the%20close()%20method