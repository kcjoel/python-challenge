#importing modules
import os
import csv

#introducing the path to our file
csvpath = os.path.join("Resources","election_data.csv")

#opening up the file within our path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header= next(csvreader)
    print(csv_header)#extracting header from data file
    
#setting up variables    
    TV=0
    CA=0
    CAL=[]
    new=[]
    cand2_count = cand1_count = cand3_count = 0
    cand1_perc= cand1_perc = cand3_perc =0
#used new to see all candidiates who received votes
    cand1="Diana DeGette"
    cand2="Raymon Anthony Doane"
    cand3="Charles Casper Stockham"
    
   
    
    
#extracts our data in rows and columns
    for row in csvreader:
        TV=TV+1
        if CA != row[2]:
            CA=row[2]
            CAL+=[CA]
            new=set(CAL)
    

#candidiate calculation for amount of votes received
    
        if row[2]==cand1:
            cand1_count= cand1_count+1
        elif cand2==row[2]:
            cand2_count= cand2_count+1
        elif row[2]== cand3:
            cand3_count= cand3_count+1
            
#candidiate calculation for the percentage of votes each candidiates received

    cand1_perc= round((cand1_count/TV)*100,3)  
    cand2_perc= round((cand2_count/TV)*100,3) 
    cand3_perc= round((cand3_count/TV)*100,3) 
    
#creating a dictionary so we can extract maximum value based on candidiates
    results={cand1:cand1_count,cand2:cand2_count,cand3:cand3_count}
    winner=max(results,key=results.get)
    
#Extracting results as CSV file
    
    output_path= os.path.join("analysis","FA2.txt")
with open(output_path,'w') as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('-----------------------\n')
    txtfile.write(f'Total Votes: {TV}\n')  
    txtfile.write('-------------------------\n')
    txtfile.write(f'{cand3}: {cand3_perc}% {cand3_count}\n')
    txtfile.write(f'{cand1}: {cand1_perc}% ({cand1_count})\n')
    txtfile.write(f'{cand2}: {cand2_perc}% ({cand2_count})\n')
    txtfile.write('----------------------\n')
    txtfile.write(f'Winner: {winner}\n')
    txtfile.write('-----------------------')