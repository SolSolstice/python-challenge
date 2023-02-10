                                                                                                                                 # Challenge 3 - Python - PyBank
                                                                                                                                 # Matthew Copello
                                                                                                                                 # ~Solstice 

import os 
import csv

csv_path = os.path.join('Resources','budget_data.csv')     

mo_count = 0
net_total = 0 
value_list = []
month_list = []
min_value = float
max_value = float
average_value = float
value_list2 = []
value_list3 = []
new_values = []
min_delta = [0,''] #list w/ 2 values.. monthly increase,month we're looking at 
max_delta = [0,'']
prevrev = 0
total_ch = 0
change = 0
current_delta = 0
rev = 0 
net_delta = 0  
min_delta = [0,''] #list w/ 2 values.. monthly increase,month we're looking at 
max_delta = [0,'']


with open(csv_path,'r',encoding='utf-8') as budget_csv: 

    budget_csv = csv.reader(budget_csv,delimiter=',')
    csvheader = next(budget_csv)
   

    prev_pl = 0 
    for i,row in enumerate(budget_csv):
        mo_count += 1
        rev = float(row[1])
        net_total += rev
        value_list.append(rev)
        month_list.append(row[0])
        value_list.append(int(row[1]))
         
        #determines where to start. looking for the first value, find where previous revenue is 0  
        if i > 0:
           current_delta = int(rev) - int(prev_pl)
           #print(current_delta)
           net_delta += int(row[1]) - int(prev_pl)
           
           # greatest delta increase
        if current_delta > max_delta[0]:
            max_delta[0] = current_delta
            max_delta[1] = row[0]
           # greatest delta decrease 
        if current_delta < min_delta[0]:
            min_delta[0] = current_delta
            min_delta[1] = row[0]

        prev_pl = rev



    

       
     # #determines where to start. looking for the first value, find where previous revenue is 0 
    #change = rev - prevrev
   # if prevrev == 0:
   #     change == 0 
  #  total_ch += change
            # ^^^ total_ch = total_ch + change

    # greatest increase
  #  if  change > max_delta[0]:
    #    max_delta[0] = change
   #     max_delta[1] = row[0]

    # greatest decrease
  #  if  change < min_delta[0]:
   #     min_delta[0] = change
     #   min_delta[1] = row[0]
   #                                      # NEED TO FIND AVERAGE CHANGE ... 
                                        # something wrong with total_ch -> only capturing the last value in list (382539)  

        prevrev = rev
print(csvheader)
#print(firstrow)
print(total_ch)

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


#~~~~~~!!!!!!!~~~~~~~~~
#print(list_of_dict)

#^ Why does it print only 1 row when here 
  #     print(list_of_dict)
 #      
   #             ^ but all rows when here?
