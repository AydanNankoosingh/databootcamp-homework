import csv


# open and read csv file
with open("Resources/election_data.csv", newline = "") as file:
    data = csv.reader(file, delimiter = ",")

    #skip header
    next(data, None)
    # append rows to list
    values = [row for row in data]


# Initializing total votes
total_votes = 0

# identifying candidates and counting votes
candidates = []
num_votes = []

for i in range(len(values)):
    if values[i][2] in candidates:
        num_votes[candidates.index(values[i][2])] += 1
    else:
        candidates.append(values[i][2])
        num_votes.append(1)
    total_votes += 1

# calculating % votes
perc_votes = [round(val/total_votes * 100, 4) for val in num_votes]

# finding the winner
winner = candidates[num_votes.index(max(num_votes))]

# printing results to terminal
print(f"""
Election Results:
-----------------------
Total Votes: {total_votes}
-----------------------
""")
for j in range(len(candidates)):
    print(f"{candidates[j]}: %{perc_votes[j]} ({num_votes[j]})")
print(f"""
-----------------------
Winner: {winner}
-----------------------
""")

# write results to a text file
results = open('Election Results.txt', 'w')
results.write(f"""
Election Results:
-----------------------
Total Votes: {total_votes}
-----------------------
""")
for j in range(len(candidates)):
    results.write(f"{candidates[j]}: %{perc_votes[j]} ({num_votes[j]})\n")
results.write(f"""
-----------------------
Winner: {winner}
-----------------------
""")
results.close()
