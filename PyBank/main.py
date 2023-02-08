                                                                                                                                #Challenge 3 - Python 
                                                                                                                                #Matthew Copello
                                                                                                                                # ~ Solstice 


import os 
import csv

csv_path = os.path.join('Resources','budget_data.csv')

row_count = 0
net_total = 0 
value_list = []
value_index = []
month_list = []
month_index = []
min_value = float
max_value = float
average_value = float


with open(csv_path,'r',encoding='utf-8') as budget_csv: 

    budget_csv = csv.reader(budget_csv,delimiter=',')


    csvheader = next(budget_csv)

    print ("Financial Analysis")
    print ("--------------------------------")

        
    for row in budget_csv:
        row_count += 1
        net_total += float(row[1])
        value_list.append(row[1])
        month_list.append(row[0])
        max_value = max(value_list, key=float)
        min_value = min(value_list, key=float)
        value_list.index(max_value)
        value_list.index(min_value)
        max_month = value_list.index(max_value)
        min_month = value_list.index(min_value)
        average_value = net_total/row_count
        



#print(month_list[11])  #
#print(month_list[38])     #
#print(max_month)            #  Searching for correct index location 
#print(value_list)          #
#print(type(month_list))  #

   


'''    

~~~~~~!!!!!!!~~~~~~~~~
print(list_of_dict)

^ Why does it print only 1 row when here 
       print(list_of_dict)
       
                ^ but all rows when here?

~~~~~~!!!!!!!~~~~~~~~~~~               
'''



print (f"The amount of Months in this CSV is: {row_count}")

print (f"The net total is: $ {net_total:,.2f}")

print(f"The average change is $ {average_value:,.2f}")

print (f"Greatest Increase in Profits: {month_list[38]} (${max_value})")    

print (f"Greatest Decrease in Profits: {month_list[11]} (${min_value})")


        




  

