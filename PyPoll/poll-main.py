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
    
    
    #for can in candidate:
    khan_vote = candidate.count('Khan')
    li_vote = candidate.count('Li')
    otool_vote = candidate.count("O'Tooley")
    correy_vote = candidate.count('Correy')
    print(khan_vote)
    print(li_vote)
    print(otool_vote)
    print(correy_vote)
    
    khan_per = round(((khan_vote / votescast)*100), 3)
    li_per = round(((li_vote / votescast)*100), 3)  
    otool_per = round(((otool_vote / votescast)*100), 3)
    correy_per = round(((correy_vote / votescast)*100), 3)
    print(khan_per, li_per, otool_per, correy_per)