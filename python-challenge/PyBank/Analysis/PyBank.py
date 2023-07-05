import os
import csv
import pandas as pd

pd.__version__

pybank_csv = os.path.join("..", "Resources", "budget_data.csv")



# # Set Dataframe
df=pd.read_csv(pybank_csv)

# Find number of rows
Months = len(df.index)

# Sum total of column
TotalPL=df['Profit/Losses'].sum()

# Create shifted column
df['shifted_column'] = df['Profit/Losses'].shift(1)

# Find difference between two colums for month to month differece
df['difference'] = df['Profit/Losses'] - df['shifted_column']

# Set value for average difference
average = df['difference'].mean()

# Find max difference
maxchng = df['difference'].max()

# Find min difference
minchng = df['difference'].min()

# Find date value for Max and Min change
MaxDate = df[df['difference']==maxchng]['Date'].values[0]
MinDate = df[df['difference']==minchng]['Date'].values[0]

# Format to currency
PLMoney="${:,.2f}".format(TotalPL)
AvgChng="${:,.2f}".format(average)
MinMoney="${:,.2f}".format(minchng)
MaxMoney="${:,.2f}".format(maxchng)

print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: ", Months)
print("Total Profits", PLMoney)
print("Average Change", AvgChng)
print("Greatest Increase in Profits:", MaxDate, "(",MaxMoney,")")
print("Greatest Decrease in Profits:", MinDate, "(",MinMoney,")")


# Output to txt file
with open("Analysis.txt", "w") as txt_file:

    txt_file.write("----------------------------------------------------------\n")
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------------------------------------\n")
    txt_file.write(f"Total Months:  {Months}\n")
    txt_file.write(f"Total Profits {PLMoney}\n")
    txt_file.write(f"Average Change {AvgChng}\n")
    txt_file.write(f"Greatest Increase in Profits: {MaxDate} ({MaxMoney})\n")
    txt_file.write(f"Greatest Decrease in Profits: {MinDate} ({MinMoney})\n")