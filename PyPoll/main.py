import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    total = 0
    county = []
    candidates = []
    votes = []
    mydict = {}
    results = []
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    #loop for data
    for row in csvreader: 
        #total votes count
        total += 1

        #add all numbers in column to votes list
        votes.append(row[0])
        #add all counties in column to county list
        county.append(row[1])
        #add all candidates in column to candidates list
        candidates.append(row[2])

    #for loop to get rid of duplicate names and put into dictionary    
    for name in candidates:
        if not name in mydict:
            mydict[name] = 1
        else:
            mydict[name] +=1


    #for each candidate and their votes in mydict
    for i, v  in mydict.items():
        #calculate average votes 
        average = ((v/total)*100)

        #mydict contents as output variable
        output = (f' {i}: {average:.3f}% ({v})')
        #append output to results list
        results.append(output)

        #winner based on popular vote
        most_popular = max(zip(mydict.values(), mydict.keys()))[1]


print("Election Results\n")
print("-----------------------\n")
print("Total Votes:", total)
print("\n-----------------------")
for each in results:
    print("\n",each)
print("\n-----------------------\n")                                                                                       
print(f'Winner: {most_popular}')
print("\n-----------------------")


output_file = os.path.join ('Analysis', "Poll_Analysis.txt")

with open(output_file, "w") as f:
    f.write("Election Results\n")
    f.write("-----------------------\n")
    f.write(f'Total Votes: {total}')
    f.write("\n-----------------------")
    for each in results:
        f.write(f'\n{each}')
    f.write("\n-----------------------\n")                                                                                       
    f.write(f'Winner: {most_popular}')
    f.write("\n-----------------------")
    