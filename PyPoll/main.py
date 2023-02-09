                                                                                                                                 # Challenge 3 - Python - PyPoll
                                                                                                                                 # Matthew Copello
                                                                                                                                 # ~Solstice 

import os 
import csv

csv_path = os.path.join('Resources','election_data.csv')

row_count = 0
results_list = []
candidate_list = []
charles_count = 0
diana_count = 0
raymon_count = 0


with open(csv_path,'r',encoding='utf-8') as election_csv:

    election_csv = csv.reader(election_csv,delimiter=',')
    csvheader = next(election_csv)
   
    for row in election_csv:
        row_count += 1
                #Note: row_count +=1 takes place of #row_count = row_count + 1
        results_list.append(row)
        
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            #checking all rows for unique candidate names and adding them to a list 
        if row[2] == 'Charles Casper Stockham':
            charles_count += 1
        if row[2] == 'Diana DeGette':
            diana_count += 1
        if row[2] == 'Raymon Anthony Doane':
            raymon_count += 1
        

charlespercent = charles_count/row_count
charlespercent = charlespercent * 100

dianapercent = diana_count/row_count
dianapercent = dianapercent * 100

raymonpercent = raymon_count/row_count
raymonpercent = raymonpercent * 100

print ("")
print ("Election Results")
print ("------------------------------------")
print("")
print (f"Total Votes: {row_count}" )
print("")
print ("------------------------------------")
print(f"Charles Casper Stockham: {charlespercent:,.2f} ({charles_count})")
print(f"Diana DeGette: {dianapercent:,.2f} ({diana_count})")
print(f"Raymon Anthony Doane: {raymonpercent:,.2f} ({raymon_count})")
print ("------------------------------------")
print("")
print("Winner: Charles Casper Stockham")
print("")
print ("------------------------------------")


#print(candidate_list)
#print(results_list)
#print(row_count)



'''

~~~~~~~~~!!!!!!!!~~~~~~~~~~~
 if row[0] == ' ' or 0:
            #missing_values = (row[0].index)
    
  !! ^ What if i wanted to check for missing data in the csv? 

~~~~~~~~~~!!!!!!!!~~~~~~~~~~~~
'''