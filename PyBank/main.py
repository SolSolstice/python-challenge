                                                                                                                                 # Challenge 3 - Python - PyBank
                                                                                                                                 # Matthew Copello
                                                                                                                                 # ~Solstice 

import os 
import csv

csv_path = os.path.join('Resources','budget_data.csv')     

row_count = 0
net_total = 0 
value_list = []
month_list = []
min_value = float
max_value = float
average_value = float
value_list2 = []
value_list3 = []
new_values = []
inc = [0,''] #list w/ 2 values.. monthly increase,month we're looking at 
dec = [0,'']
prevrev = 0
total_ch = 0

with open(csv_path,'r',encoding='utf-8') as budget_csv: 

    budget_csv = csv.reader(budget_csv,delimiter=',')
    csvheader = next(budget_csv)

   
    for row in budget_csv:
        row_count += 1
        rev = float(row[1])
        net_total += rev
        value_list.append(rev)
        month_list.append(row[0])
        max_value = max(value_list, key=float)
        min_value = min(value_list, key=float)
        value_list.index(max_value) #for finding the index of max_value
        value_list.index(min_value) #for finding the index of min_value
        #max_month = value_list.index(max_value)
       # min_month = value_list.index(min_value)

        # #determines where to start. looking for the first value, find where previous revenue is 0 
        change = rev - prevrev
        if prevrev == 0:
            change == 0 
        total_ch += change
                 # ^^^ total_ch = total_ch + change

        # greatest increase
        if (change > inc[0]):
            inc[0] = change
            inc[1] = row[0]

        # greatest decrease
        if (change < dec[0]):
            dec[0] = change
            dec[1] = row[0]
        
        prevrev = rev 





print ("")
print ("Financial Analysis")
print ("----------------------------------------------")
print ("")
print (f"Total Months: {row_count}")
print("")
print (f"Net Total: $ {net_total:,.2f}")
print("")
print(f"Average Change: $ {total_ch/(row_count-1):,.2f}")
print("")
print (f"Greatest Increase in Profits: {inc[1]} ($ {inc[0]})")    
print("")
print (f"Greatest Decrease in Profits: {dec[1]} ($ {dec[0]})")
print ("-----------------------------------------------")

'''    

~~~~~~!!!!!!!~~~~~~~~~
print(list_of_dict)

^ Why does it print only 1 row when here 
       print(list_of_dict)
       
                ^ but all rows when here?

~~~~~~!!!!!!!~~~~~~~~~~~               
'''
        

