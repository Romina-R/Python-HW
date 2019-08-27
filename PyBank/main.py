import os
import csv
import statistics

date = []
profit_loss = []

PyBankHW = os.path.join("Resources", "budget_data.csv")

with open(PyBankHW, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    totalmoney = 0
    for row in csvreader:  
        date.append(row[0])
        profit_loss.append(int(row[1]))
        
    # WORKS, DONT CHANGE!!!! -----------------------
        totalmoney += float(row[1])

    # WORKS, DONT CHANGE!!!! -----------------------
    change = []
    for x in range(1,len(profit_loss)):
        changes = ((profit_loss[x]) - (profit_loss[x-1]))
        change.append(changes)
 
    averagechange = round(statistics.mean(change),2)

    maxincrease = max(change)
    maxloss = min(change)
   
    maxincrease_index = change.index(maxincrease)
    maxloss_index = change.index(maxloss)


    #for x in change:
        #print(max(change()))
    #print(min(change()))     
    

#newtable = list(zip(date, profit_loss, change))

#maxprofit = max(newtable[2])
#print(maxprofit)
    #maxprofit = max(profit_loss)

totalmonths = len(date)
    
print("Financial Analysis")
print("---------------------------------------------------------")
print(f"Total Months: {totalmonths}")    
print(f"Average Change: ${averagechange}")
print(f"Total: ${totalmoney}") 
print(f"Greatest Increase in Profits: {date[maxincrease_index+1]} $({maxincrease})")
print(f"Greatest Decrease in Profits: {date[maxloss_index+1]} $({maxloss})")  

#-----------------------WRITE---------------------------
output_file = os.path.join("RR_output_file.txt")

with open(output_file, "w") as textfile:


    textfile.write("Financial Analysis")
    textfile.write("------------------------------------------------------------")
    textfile.write(f"Total Months: {totalmonths}")    
    textfile.write(f"Average Change: ${averagechange}")
    textfile.write(f"Total: ${totalmoney}") 
    textfile.write(f"Greatest Increase in Profits: {date[maxincrease_index+1]} $({maxincrease})")
    textfile.write(f"Greatest Decrease in Profits: {date[maxloss_index+1]} $({maxloss})")