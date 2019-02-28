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

#create empty list named date_table    
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
    print(avg_change)      
   
    
    
    
         
        
        
        
    
    
    
    


    
        
#total_record = len(csv_reader)
        #records = (','.join(row))
        #print(records)
#print(type(records))        
   
    
    #Table = []
    #Table.append(records) 
    #print(Table)
    
        #print(records)
    
  
    
        
        #records.append(row) 
        #dates = set(rows(0))
        #print(dates)
        #month_tot = len(rows)
        #print(month_tot)
    