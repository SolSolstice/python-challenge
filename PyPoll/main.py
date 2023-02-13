                                                                                                                    # Challenge 3 - Python - PyPoll
                                                                                                                    # Matthew Copello
                                                                                                                    # ~Sol
import os 
import csv

csv_path = os.path.join('Resources','election_data.csv')

textpath = "election_results.txt"
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

with open(os.path.join('Analysis','election_results.txt'), "w") as file:

    file.write("Election Results\n")
    file.write("------------------------------------\n")
    file.write(f"Total Votes: {row_count}\n" )
    file.write("------------------------------------\n")
    file.write(f"Charles Casper Stockham: % {charlespercent:,.3f} ({charles_count})\n")
    file.write(f"Diana DeGette: % {dianapercent:,.3f} ({diana_count})\n")
    file.write(f"Raymon Anthony Doane: % {raymonpercent:,.3f} ({raymon_count})\n")
    file.write("------------------------------------\n")
    file.write("Winner: Diana DeGette\n")
    file.write("------------------------------------\n")

print ("")
print ("Election Results")
print ("------------------------------------")
print("")
print (f"Total Votes: {row_count}" )
print("")
print ("------------------------------------")
print(f"Charles Casper Stockham: % {charlespercent:,.3f} ({charles_count})")
print(f"Diana DeGette: % {dianapercent:,.3f} ({diana_count})")
print(f"Raymon Anthony Doane: % {raymonpercent:,.3f} ({raymon_count})")
print ("------------------------------------")
print("")
print("Winner: Diana DeGette")
print("")
print ("------------------------------------")