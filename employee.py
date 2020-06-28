# ########################################################################################
# Restructure Employee Data
# ########################################################################################

##########################################################################################
################################### Imports ##############################################

import os    # Module to create file paths across operating systems
import csv   # Module to read CSV files
import time  # Track time for program to execute

start_time = time.process_time()  # Track Time (start)

##########################################################################################
################################# Data Extract ###########################################

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


csvpath = os.path.join('Data', 'employee_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Header row:  Voter ID,County,Candidate
    header_row = next(csvreader)

    employee_data=[]
    
    for row in csvreader:
        # Start:  ['Emp ID', 'Name', 'DOB', 'SSN', 'State']
        # End:    ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']

        employee_ID=row[0]
        name=row[1].split()
        first_name=name[0]
        last_name=name[1]
        date=row[2].split("-")
        year=date[0]
        month=date[1]
        day=date[2]
        dob=f"{month}-{day}-{year}"
        ssn=f"***-**-{row[3].split('-')[2]}"
        state=row[4]
        abbrev=us_state_abbrev[state]

        employee_data =f"{employee_ID}, {first_name}, {last_name}, {dob}, {ssn}, {abbrev}\n"
        print(employee_data)
        

        with open('output.txt', 'a+') as fin:
            fin.write(employee_data)


