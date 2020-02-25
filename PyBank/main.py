# Import the csv
import os 
import csv 
budget_csv = os.path.join("Resources", "budget_data.csv")

# Define Variables
total_months = 0
total_revenue = 0

prev_revenue = 0
revenue_change = 0
revenue_month = []
revenue_changes = []

greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999999999999999999999999999999999999]

# Open File in Python 
with open(budget_csv) as budget_data:
    reader = csv.DictReader(budget_data)

    # For loop to look through data 
    for row in reader:

        # Get Total Amount of Months/Revenue
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])
        revenue_month.append(int(row["Profit/Losses"]))
        
        # Figure out how to calculate the revenue change in bewtween months 
        revenue_change = int(row["Profit/Losses"]) - prev_revenue                  
    
        #Determine the greatest increase in profit
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row["Date"]
        #Determine the greatest decrease in profit
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row["Date"]
        
        # Change the previous values so that we take into account the changing values for months 
        prev_revenue = int(row["Profit/Losses"])   
    
    # 2nd For loop to look through data for Average Change in month per month
    for i in range(len(revenue_month)-1): 
        revenue_change = revenue_month[i+1]-revenue_month[i] 
        revenue_changes.append(revenue_change)
    avg = sum(revenue_changes)/len(revenue_changes)
  
    
    #Show Financial Analysis
    print(f'Financial Analysis')
    print(f'-------------------------------------------------')
    print(f'Total Months: {str(total_months)} Months')
    print(f'Total Revenue: $ {str(total_revenue)}')
    print(f'Average Change in Revenue: ${str(round(avg, 2))}')
    print(f'Greatest Increase in Profits: {str(greatest_increase[0])} ${str(greatest_increase[1])}') 
    print(f'Greatest Decrease in Profits: {str(greatest_decrease[0])} ${str(greatest_decrease[1])}')

#Output the Financial Analysis to text 
outputfile = open("Financial Analysis.txt", "w")
outputfile.write(f'Financial Analysis')
outputfile.write("\n")
outputfile.write(f'-----------------------------------')
outputfile.write("\n")
outputfile.write(f'Total Months: {str(total_months)} Months')
outputfile.write("\n")
outputfile.write(f'Total Revenue: $ {str(total_revenue)}')
outputfile.write("\n")
outputfile.write(f'Average Change in Revenue: ${str(round(avg, 2))}')
outputfile.write("\n")
outputfile.write(f'Greatest Increase in Profits: {str(greatest_increase[0])} ${str(greatest_increase[1])}') 
outputfile.write("\n")
outputfile.write(f'Greatest Decrease in Profits: {str(greatest_decrease[0])} ${str(greatest_decrease[1])}')
outputfile.close()