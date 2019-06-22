# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                                                 #
#                          WHITEBOARDING FOR UNIT 3 HOMEWORK  -  PyBank                           #
#                                                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# import the bank data
# count the number of months in data set (this will be the number of rows, less 1 for the header)
# calculate the net total for the profit/loss of the entire period (this will be a sum of the total PnL column)
# calculate the average for PnL of the entire period (results of line 9 divided by line results of line 8)
# find the greatest increase in profits in the entire period (this will be the highest value in the set) & date it occurred
# find the greatest decrease in profits in the entire period (this will be the lowest value in the set) & date it occurred
# print results to both the terminal and to a text file

# bank_data file is
# 2 columns [Date, Profit/Losses]
# this is included in a header row



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  PyBank CODE                                                                                    #  
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# import the bank data
import os
import csv

bank_data_path = os.path.join('budget_data.csv')

with open(bank_data_path, 'r', newline='') as csvfile:
    bank_data = csv.reader(csvfile, delimiter=',')
    header = next(bank_data) # since skipping, all value counts below are true, no need to subtract 1 for header in math...
    each_month = list(bank_data)

# get length of bank data list set to provide number of months in file
    months = len(each_month)

# create independent lists for month and profit/loss
    period, pnl = list(zip(*each_month))

# grab values and cast to integers
    pnl_values = [int(x) for x in pnl]

# calculate net profit/loss
    total_pnl = 0
    for day in pnl_values:
        total_pnl += day 

# calculate change from month to month
    change = []
    i = 0
    for number in range(len(pnl_values)-1):
        var = pnl_values[i+1] - pnl_values[i]
        i += 1
        change.append(var)
    
# calculate sum of changes (for use in averaging)    
    ttl_chgs = 0
    for var in change:
        ttl_chgs += var
    
# calculate average change; divide by 1 less than number of months since there is no change value for first month    
    avg_chg = ttl_chgs / (months - 1)

# find index of min/max values; to match correct month in output, add 1 since no change value to match to month[0] 
    h = change.index(max(change))
    l = change.index(min(change))
    
    print('Financial Analysis')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - -')
    print('Total Months: ', months)
    print('Total: ', '${}'.format(int(total_pnl)))
    print('Average Change: ', '${:.2f}'.format(float(avg_chg)))
    print('Greatest Increase in Profits: ', period[h+1], ' ${}'.format(max(change)))
    print('Greatest Decrease in Profits: ', period[l+1], ' ${}'.format(min(change)))
    print('- - - - - - - - - - - - - - - - - - - - - - - - - -')    
    
    with open('FinancialAnalysis.txt', 'w') as f:    
        print('Financial Analysis', file=f)
        print('- - - - - - - - - - - - - - - - - - - - - - - - - -', file=f)
        print('Total Months: ', months, file=f)
        print('Total: ', '${}'.format(int(total_pnl)), file=f)
        print('Average Change: ', '${:.2f}'.format(float(avg_chg)), file=f)
        print('Greatest Increase in Profits: ', period[h+1], ' ${}'.format(max(change)), file=f)
        print('Greatest Decrease in Profits: ', period[l+1], ' ${}'.format(min(change)), file=f)
        print('- - - - - - - - - - - - - - - - - - - - - - - - - -', file=f)