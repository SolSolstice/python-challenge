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
with open(csv_path,'r',encoding='utf-8') as budget_csv: 

    budget_csv = csv.reader(budget_csv,delimiter=',')
    csvheader = next(budget_csv)

   
    for row in budget_csv:
        row_count += 1
        net_total += float(row[1])
        value_list.append(float(row[1]))
        month_list.append(row[0])
        max_value = max(value_list, key=float)
        min_value = min(value_list, key=float)
        value_list.index(max_value) #for finding the index of max_value
        value_list.index(min_value) #for finding the index of min_value
        max_month = value_list.index(max_value)
        min_month = value_list.index(min_value)
      


 #################################################

    #trying to figure out  "The changes in "Profit/Losses" over the entire period, and then the average of those changes"
 
#~~~~~~~~~~!!!!!!!!~~~~~~~~~~~
# This appears to work?? Not sure why.. or if the values are correct..  would rather come up with a different solution... 
#
differences = value_list[0]; [-differences + (differences := x) for x in value_list[1:]]
#print(differences)
average_differences = differences/row_count-1
#print(average_differences)

# ~~~~~~~~~~~~!!!!!!~~~~~~~~~
    # this appeared to *almost* work.. numbers didnt seem to add (or subtract) correctly.. 
#i = 0
#for n in value_list:
#    i = (i) + (n+1)
 #   print(n)


#########################################################





#print(month_list[11])  #
#print(month_list[38])     #
#print(max_month)            #  Searching for correct index location 
#print(value_list)          #
#print(type(month_list))  #

#print(value_list)


print ("")
print ("Financial Analysis")
print ("----------------------------------------------")
print ("")
print (f"Total Months: {row_count}")
print("")
print (f"Net Total: $ {net_total:,.2f}")
print("")
print(f"Average Change: $ {average_differences:,.2f}")
print("")
print (f"Greatest Increase in Profits: {month_list[38]} ($ {max_value})")    
print("")
print (f"Greatest Decrease in Profits: {month_list[11]} ($ {min_value})")
print ("-----------------------------------------------")

'''    

~~~~~~!!!!!!!~~~~~~~~~
print(list_of_dict)

^ Why does it print only 1 row when here 
       print(list_of_dict)
       
                ^ but all rows when here?

~~~~~~!!!!!!!~~~~~~~~~~~               
'''
        

