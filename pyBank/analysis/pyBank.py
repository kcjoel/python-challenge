import os
import csv

#introducing the path to our file
csvpath = os.path.join("Resources","budget_data.csv")

#opening up the file within our path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header= next(csvreader)
    print(csv_header)#extracting header from data file
    
#setting up variables    
    TM=0 #Total Month
    TPL=0 #Total Profit/Loss
    y1=0 #first item for profit/loss
    changeNet=[] 
    great_inc=['',0] #Used for calculating greatest P/L increase change
    great_dec=[0,99999999999] #Used for calculating the greatest P/L decrease
    PNet = 0
  
#extracts our data in rows and columns
    for row in csvreader:
        print(row[0],row[1])
        TM=TM+1
        TPL= TPL+float(row[1])
        
#calculating data used for average profit/loss        
        if TM==1:
            y1=float(row[1])
            
#Tracking the change in profit/loss    
        change= float(row[1])-PNet
        PNet=float(row[1])
        changeNet+= [change]
       
        
#calculating the greatest increase
        if change > great_inc[1]:
            great_inc[0] = row[0]
            great_inc[1]=  change
        
#calculating the greatest decrease
        if change < great_dec[1]:
            great_dec[0] = row[0]
            great_dec[1]=  change
            
#calculating the average change        
    AC=(float(row[1])-y1)/(TM-1)

#exporting our final results to a CSV file
output_path= os.path.join("analysis","FA1.txt")
with open(output_path,'w') as txtfile:
    txtfile.write("FINANCIAL ANALYSIS\n")
    txtfile.write('-----------------------\n')
    txtfile.write(f'Total Months:  {TM}\n')
    txtfile.write(f'Total:  ${TPL}\n')  
    txtfile.write(f'Average Change:  ${AC}\n')
    txtfile.write(f'Greatest Increase in Profits: {great_inc[0]} (${great_inc[1]})\n')
    txtfile.write(f'Greatest Decrease in Profits: {great_dec[0]} (${great_dec[1]})')