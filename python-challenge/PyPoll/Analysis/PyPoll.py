import os
import csv
import pandas as pd

pd.__version__


election_csv = os.path.join("..", "Resources", "election_data.csv")

with open(election_csv) as csv_file:

    df=pd.read_csv(election_csv)

    # Find total number of votes
    VoteTotal = len(df.index)

    # Set candidate Name value as list
    Candidates = df['Candidate'].unique()

    # Find individual candidate vote counts
    ChuckCount = df["Candidate"].value_counts()['Charles Casper Stockham']
    DianaCount = df["Candidate"].value_counts()['Diana DeGette']
    RayCount = df["Candidate"].value_counts()['Raymon Anthony Doane']

    # Find individual candidate percentage
    ChuckPerc = "{:.3%}".format(ChuckCount/VoteTotal)
    DianaPerc = "{:.3%}".format(DianaCount/VoteTotal)
    RayPerc = "{:.3%}".format(RayCount/VoteTotal)

    # Find candidate with highest vote total
    Winner = df["Candidate"].value_counts().idxmax()

print("----------------------------------------------------------")
print("Election Results")
print("----------------------------------------------------------")
print("Total Votes:", VoteTotal)
print("----------------------------------------------------------")
print(f"{Candidates[0]}: {ChuckPerc} ({ChuckCount})")
print(f"{Candidates[1]}: {DianaPerc} ({DianaCount})")
print(f"{Candidates[2]}: {RayPerc} ({RayCount})")
print("----------------------------------------------------------")
print(f"Winner: {Winner}")
print("----------------------------------------------------------")

with open("Analysis.txt", "w") as txt_file:

    txt_file.write("----------------------------------------------------------\n")
    txt_file.write("Election Results\n")
    txt_file.write("----------------------------------------------------------\n")
    txt_file.write(f"Total Votes: {VoteTotal}\n")
    txt_file.write("----------------------------------------------------------\n")
    txt_file.write(f"{Candidates[0]}: {ChuckPerc} ({ChuckCount})\n")
    txt_file.write(f"{Candidates[1]}: {DianaPerc} ({DianaCount})\n")
    txt_file.write(f"{Candidates[2]}: {RayPerc} ({RayCount})\n")
    txt_file.write("----------------------------------------------------------\n")
    txt_file.write(f"Winner: {Winner}\n")
    txt_file.write("----------------------------------------------------------\n")
