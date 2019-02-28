#import os module to retrieve data file 
import os

#set path to data file
csvpath = os.path.join("..", "..", "..", "Python_HW_Data", "PyPoll_Resources_election_data.csv")

#confirm file path is correct
print(os.path.isfile(csvpath))

#import csv module to open file and read data
import csv
with open(csvpath, newline="")as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

#confirm availability of file data    
    #print(csv_reader)

#skip header
    csv_header = next(csvfile) 
    print(csv_header)
            
#create empty lists: 
    voterID = []
    county = []
    candidate = []
    
#add Voter ID data to voterID list 
#add County data to county list
#add Canadidate data to candidate list    
    for column in csv_reader:
        voterID.append(column[0])
        county.append(column[1])
        candidate.append(column[2])

#find total number of votes cast using len function
    votescast = len(voterID)
    print(votescast)

    candidate_list = []
    candidate_list = set(candidate)
    print(candidate_list)
    
    
    for can in candidate:
        khan_vote = candidate.count('khan')
        li_vote = candidate.count('li')
        otool_vote = candidate.count("O'Tooley")
        correy_vote = candidate.count('Correy')
   