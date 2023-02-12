import csv
with open('autos.csv') as fl:
    csvread = csv.reader(fl,delimiter=',')
    for  i in csvread:
        print(i[4],i[2],i[1])
       