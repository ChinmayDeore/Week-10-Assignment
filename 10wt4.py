## Chinmay D. 11/9/2022 Hg5590
import csv
import sys
import json
def PersistentData():
# Naming and starting the function
    with open(r'C:\Users\cesta\OneDrive\Desktop\CSC 1500\Week 10 work\SalesJan2009.csv') as i:
        reader=csv.reader(i)
# Searches files in desktop and opens the SalesJan2009 file
        sales_data=[]
        for row in reader:
            sales_data.append({'Transaction_date':row[0].strip('"'),
            'Product':row[1].strip('"'),
            'Price':row[2].strip('"'),
            'Payment_Type':row[3].strip('"'),
            'Name':row[4].strip('"'), 
            'City':row[5].strip('"'),
            'State':row[6].strip('"'),
            'Country':row[7].strip('"')})
# Iterates lines in list as a dictionary
    with open('transaction_data.json','w') as jsonf:
        json.dump(sales_data,jsonf, indent=2)
# Adds data value onto the newly created json file
PersistentData()
# Calls the function and ends the program
## HALF-LIFE, Ron Bass, John Richards Sr., After-Burner Elite