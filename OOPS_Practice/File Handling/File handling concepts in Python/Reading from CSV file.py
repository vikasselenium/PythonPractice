
import csv
with open('sample_employees.csv',"r") as f:
    csv_reader=csv.reader(f)
    print(csv_reader)
    data=list(csv_reader)
    print(data) # it returns CSV data as list of list

    for row in data:
        print(row)

    print("++++++++++++++++++++++++++++++++++")
    for row in data:
        for column in row:
            print(column, '|',end='')
        print()
    print("++++++++++++++++++++++++++++++++++")