#import os module to retrieve data file
import os

#set path to data file
csvpath = os.path.join("..", "..", "..", "Python_HW_Data", "PyBank_Resources_budget_data.csv")

#import csv module to open file and read data
import csv
with open(csvpath, newline="")as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

#skip header
    csv_header = next(csvfile) 

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
      
#change began on 2nd month, insert 0 to show 0 change value for the 1st month   
    change_list.insert(0, 0)

#zip/combine date_table list with change_list
#make a new list with above data and convert to a dictionary   
    date_change_list = zip(date_table, change_list) 
    new_date_change_list = dict(date_change_list)

#find max and min values
    grt_inc = max(new_date_change_list.items(), key = lambda x: x[1])
    a = list(grt_inc)
    grtincm = a[0]
    grtincv = a[1] 
    
    grt_dec = min(new_date_change_list.items(), key = lambda x: x[1])
    b = list(grt_dec)
    grtdecm = b[0]
    grtdecv = b[1]  
#****CONFESSION - I stole the above codes with a rudimentary understanding
#                 for I struggled to use iteration to calculate the values.
#                 I also tried using max & min functions but was not
#                 able to get the right format to print.

#print results    
    print("Financial Analysis")
    print('--------------------')
    print(f"Total Months: {total_month}")
    print(f"Total: ${plsum}")
    print(f"Average Change: ${avg_change}")
    print(f'Greatest Increase in Profits: {grtincm}, ${grtincv}')
    print(f'Greatest Decrease in Profits: {grtdecm}, ${grtdecv}')

#export results to csv file pybank_answers.csv    
output_path = os.path.join("pybank_answers.csv")
   
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Total Months:", total_month])
    csvwriter.writerow(['Total: $', plsum])
    csvwriter.writerow(['Average Change: $', avg_change])
    csvwriter.writerow(['Greatest Increase in Profits', grtincm, grtincv])
    csvwriter.writerow(['Greatest Decrease in Profits', grtdecm, grtdecv])     
       
   
    
    
    
     
    
         
        
        
       