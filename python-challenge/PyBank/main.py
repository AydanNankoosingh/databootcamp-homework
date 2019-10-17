import csv


# open and read csv file
with open("Resources/budget_data.csv", newline = "") as file:
    data = csv.reader(file, delimiter = ",")

    #skip header
    next(data, None)
    # append rows to list
    values = [row for row in data]

# finding the total number of months
num_months = len(values)

# calculating total profits
total_profit = 0
for i in range(len(values)):
    total_profit += float(values[i][1])

# calculating month-to-month changes and storing in list
changes = [float(values[j + 1][1]) - float(values[j][1]) for j in range(len(values) - 1)]

# finding the largest increase
max_inc = max(changes)

# finding the month with the largest increase
max_month = values[changes.index(max_inc) + 1][0]

# finding the largest decrease
max_dec = min(changes)

# finding the month with the largest decrease
min_month = values[changes.index(max_dec) + 1][0]

# finding the average change
avg_change = sum(changes) / len(changes)

# printing results to terminal
print(f"""
Financial Analysis:
-------------------------------------
Total Months: {num_months}
Total: {total_profit}
Average Change: ${round(avg_change, 2)}
Greatest Increase in Profits: {max_month} (${max_inc})
Greatest Decrease in Profits: {min_month} (${max_dec})
""")


# Writing results to text file
results = open('Financial Analysis.txt', 'w')
results.write(f"""
Financial Analysis:
-------------------------------------
Total Months: {num_months}
Total: {total_profit}
Average Change: ${round(avg_change, 2)}
Greatest Increase in Profits: {max_month} (${max_inc})
Greatest Decrease in Profits: {min_month} (${max_dec})
""")
results.close()
