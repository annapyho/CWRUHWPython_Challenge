#import os module to retrieve data file
import os

#set path to data file
csvpath = os.path.join("..", "..", "..", "Python_HW_Data", "PyPoll_Resources_election_data.csv")

#import csv module to open file and read data
import csv
with open(csvpath, newline="")as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

#skip header
    csv_header = next(csvfile) 
            
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
    
#use set function to find unique candidate names 
    candidate_list = []
    candidate_list = list(set(candidate))

#calculate vote count and vote percentage per candidate and store in
#voteresults dictionary        
    voteresults ={}
    for candidates in candidate_list:
        vote = candidate.count(candidates)
        voteper = (vote / votescast)
        voteresults[candidates] = vote, '{:.2%}'.format(voteper,3)

#sort results from highest to lowest    
    svr = sorted(voteresults.items(), key=lambda x:x[1],  reverse=True)
    highest_vote = max(voteresults.items(), key = lambda x: x[1])
#first value in highest vote list was declared winner
    a = list(highest_vote)
    winner = a[0]
  
#print results    
    print("Election Results")
    print('-----------------------')
    print(f"Total Votes: {votescast}")
    print('-----------------------')
    for i in range(0,len(svr)):
        print(svr[i][0], svr[i][1])
    print('-----------------------')
    print(f'Winner: {winner}')
    print('-----------------------')
    
#export results to csv file pybank_answers.csv    
output_path = os.path.join("pypoll_answers.csv")
   
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Total Votes:", votescast])
    for i in range(0,len(svr)):
        res = list(svr[i][1])
        csvwriter.writerow([svr[i][0], res[0], res[1]])
    csvwriter.writerow(['Winner', winner])