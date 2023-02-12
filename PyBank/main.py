                                                                                                                           # Challenge 3 - Python - PyBank
                                                                                                                           # Matthew Copello
                                                                                                                           # ~Sol 

import os 
import csv


csv_path = os.path.join('Resources','budget_data.csv')     

textpath = "financial_analysis.txt"
mo_count = 0
net_total = 0 
min_delta = [0,''] #list w/ 2 values.. monthly increase,month we're looking at 
max_delta = [0,'']
current_delta = 0
rev = 0 
net_delta = 0  

with open(csv_path,'r',encoding='utf-8') as budget_csv: 

    budget_csv = csv.reader(budget_csv,delimiter=',')
    csvheader = next(budget_csv)
   
    prev_pl = 0 
    for i,row in enumerate(budget_csv):   
            # using enumerate() here in order to utilize "i" as a way to index through the rows of the csv
        mo_count += 1
        rev = float(row[1])
            # rev = all the values in column B
        net_total += rev
            # net_total = net_total + all the values in column B -> stores an aggregate of column B 
        # "i" provides an eloquent solution to the crux of my problem:
        # finding the 2nd value and subtracting that from the first then subtracting the difference (aka: current_delta).  

        if i > 0:
         # Determines where to start. looking for the first value. "If i > 0" means -> If we are on the 2nd row (index 1): do this thing.            
           current_delta = int(rev) - int(prev_pl)
                        # prev_pl starts at 0 - as set above, then goes to each value in 
           net_delta += rev - int(prev_pl)
           
           # greatest delta increase
        if current_delta > max_delta[0]:
            max_delta[0] = current_delta
            max_delta[1] = row[0]
           # greatest delta decrease 
        if current_delta < min_delta[0]:
            min_delta[0] = current_delta
            min_delta[1] = row[0]

        prev_pl = rev
 
with open(textpath,'w') as file:

    
    file.write("Financial Analysis\n")
    file.write("----------------------------------------------\n")
    file.write(f"Total Months: {mo_count}\n")
    file.write(f"Net Total: $ {net_total:,.2f}\n")
    file.write(f"Average Change: $ {net_delta/(mo_count-1):,.2f}\n")
    file.write(f"Greatest Increase in Profits: {max_delta[1]} ($ {max_delta[0]})\n")
    file.write(f"Greatest Decrease in Profits: {min_delta[1]} ($ {min_delta[0]})\n")
    file.write("-----------------------------------------------\n")

print ("")
print ("Financial Analysis")
print ("----------------------------------------------")
print ("")
print (f"Total Months: {mo_count}")
print("")
print (f"Net Total: $ {net_total:,.2f}")
print("")
print(f"Average Change: $ {net_delta/(mo_count-1):,.2f}")
print("")
print (f"Greatest Increase in Profits: {max_delta[1]} ($ {max_delta[0]})")    
print("")
print (f"Greatest Decrease in Profits: {min_delta[1]} ($ {min_delta[0]})")
print ("-----------------------------------------------")