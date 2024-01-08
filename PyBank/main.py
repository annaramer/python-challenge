import os
import csv

# File paths
input_csv = os.path.join("Resources", "budget_data.csv")
output_folder = "analysis"
output_txt = os.path.join(output_folder, "financial_results.txt")

# Create the analysis folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Lists to store data
Total_Months = []
Total_Amount = []

# Open the CSV file
with open(input_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Add month to Total_Months list
        Total_Months.append(row[0])

        # Add Amount to Total_Amount list
        Total_Amount.append(int(row[1]))

# The total number of months included in the dataset
total_months = len(Total_Months)

# The net total amount of "Profit/Losses" over the entire period
net_total_amount = sum(Total_Amount)

# Calculate the changes in "Profit/Losses" over the entire period
changes = [int(b) - int(a) for a, b in zip(Total_Amount[:-1], Total_Amount[1:])]

# The average of those changes
average_change = sum(changes) / len(changes) if len(changes) > 0 else 0

# The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(changes)
increase_index = changes.index(greatest_increase)
increase_month = Total_Months[increase_index + 1]

# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(changes)
decrease_index = changes.index(greatest_decrease)
decrease_month = Total_Months[decrease_index + 1]

# Print the results to the console
print(f"Total Months: {total_months}")
print(f"Net Total Amount: {net_total_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

# Create and write results to a text file in the analysis folder
with open(output_txt, "w") as output_file:
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Net Total Amount: {net_total_amount}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n")

# Print a message indicating the export
print(f"Results exported to '{output_txt}'.")
