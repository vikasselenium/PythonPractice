# CSV files have comma separated values
# inbuilt module- csv
# column header and rows

import csv

with open('../Python Examples/emp.csv', 'a', newline="") as f:
    csv_writer=csv.writer(f)
    #print(csv_writer)
    csv_writer.writerow(["ENO","EName","ESal","EAdd"])
    while True:
        eno=int(input("Enter Emp number:"))
        e_name = input("Enter Emp Name:")
        e_sal = float(input("Enter Emp Salary:"))
        e_address=input("Enter Emp address:")
        csv_writer.writerow([eno,e_name,e_sal,e_address])
        option=input("Do you want to insert another record[yes/no]:")
        if option.lower() =='no':
            break
        print("Added record to CSV file")
