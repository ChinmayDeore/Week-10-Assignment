## Chinmay D. 11/9/2022 Hg5590
import csv
import sys
def TicketFive():
# Naming and starting the function
    with open(r'C:\Users\cesta\OneDrive\Desktop\CSC 1500\Week 10 work\SalesJan2009.csv') as x:
        newlist = csv.reader(x) 
# Searches files in desktop and opens the SalesJan2009 file
        for x in open(r'C:\Users\cesta\OneDrive\Desktop\CSC 1500\Week 10 work\SalesJan2009.csv'):
            print(x.upper(), end='')
# Manipulates file datat according to list comprehenssion and capitalizes all characters
TicketFive()
# Calls the function and ends the program
## HALF-LIFE, Ron Bass, John Richards Sr., After-Burner Elite