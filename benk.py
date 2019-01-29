import argparse #importerar argparse så att vi kan använda den funktionen.
import datetime
import csv #importerar csv

parser = argparse.ArgumentParser() #förkortar
parser.add_argument("-f", "--file", help="filename.csv") #lägger till ett argument till programmet
args = parser.parse_args() #förkortar parser.parse_args() till args.
print(args.file) #printar ut filnamnet 

with open(args.file, newline='') as csvfile: #öppnar filen som csv fil
    reader = csv.DictReader(csvfile) #förkortar.
    for row in reader: #en loop som används tills listan är helt up printad
        print(row['first_name'][0:3] + row['last_name'][0:3]) #printar ut raderna.


x = datetime.datetime.now()
print(x.year)    