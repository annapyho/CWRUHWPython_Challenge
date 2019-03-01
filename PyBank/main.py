#import os module to retrieve data file 
import os

#set path to data file
csvpath = os.path.join("..", "..", "..", "Python_HW_Data", "PyBank_Resources_budget_data.csv")

#confirm file path is correct
print(os.path.isfile(csvpath))

#import csv module to open file and read data
import csv
with open(csvpath, newline="")as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

#confirm availability of file data    
    print(csv_reader)

#skip header
    csv_header = next(csvfile) 
    print(csv_header)

#create empty lists: date_table & btmline_table   
    date_table = []
    btmline_table = []
    
#add date data to date_table (list) 
#add P&L data to btmline_table (list)
#Cast btmline_table data to integer  
    for column in csv_reader:
        date_table.append(column[0])
        btmline_table.append(column[1])
    btmline_table = [int(i) for i in btmline_table]
    
#find total months using len function
#use while loop to calculate P&L total        
    total_month = (len(date_table))
    counter = 0
    plsum = 0
    for i in btmline_table:
        while counter < total_month:
            plsum = plsum + btmline_table[counter]
            counter += 1   

#use while loop to calulate month-over-month change
#create change_list (empty list) to store change values
#sum values in change_list & calculate average of the changes            
    counter = 0
    change_list = []
    change_sum = 0
    for i in btmline_table:
        while counter < (total_month - 1):
            change = btmline_table[counter+1]-btmline_table[counter]
            change_list.append(change)
            change_sum = change_sum + change_list[counter]
            counter += 1
    avg_change = round((change_sum / (total_month - 1)), 2) 
    #print(avg_change)      
   
    
  
    change_list.insert(0, 0)
    #print(change_list)
    #print(date_table)
    date_change_list = zip(date_table, change_list) #here
    new_date_change_list = dict(date_change_list)
   
    grt_inc = max(new_date_change_list.items(), key = lambda x: x[1])
    print(grt_inc)
    
    grt_dec = min(new_date_change_list.items(), key = lambda x: x[1])
    print(grt_dec)
        
                    
    grt_inc = [max(date_change_list)]
    #print(grt_inc)
    #print(type(grt_inc))    
   # date_change_list = zip(change_list, date_table) 
    #grt_dec = [min(date_change_list)]
    #print(grt_dec)
    #print(type(grt_dec))
     
    
    
    
#print results    
   # print("Financial Analysis")
   # print('--------------------')
   # print(f"Total Months: {total_month}")
    #print('Total: $', plsum)
    #print('Average Change: $', avg_change)
    #print('Greatest Increase in Profits: $', grt_inc)
    #print('Greatest Decrease in Profits: $', grt_dec)

#export results to csv file pybank_answers.csv    
output_path = os.path.join("pybank_answers.csv")
   
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Total Months:", total_month])
    csvwriter.writerow(['Total: $', plsum])
    csvwriter.writerow(['Average Change: $', avg_change])
    csvwriter.writerow(['Greatest Increase in Profits', grt_inc])
    csvwriter.writerow(['Greatest Decrease in Profits', grt_dec])     
       
   
    
    
    
     
    
         
        
        
       