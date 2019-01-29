import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", help="filename.csv")
args = parser.parse_args()
print(args.file)
import csv
with open(args.file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        print(row)