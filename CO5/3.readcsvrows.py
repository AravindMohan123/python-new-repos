import csv
with open('autos.csv') as fl:
    csvread = csv.reader(fl,delimiter=',')
    for  i in csvread:
        print(i)
