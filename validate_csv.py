import csv
import sys

csv_file_path = sys.argv[1]

try:
    with open(csv_file_path, 'r') as file:
        dialect = csv.Sniffer().sniff(file.read())
        file.seek(0)
        print("true")
except csv.Error:
    print("Invalid file format. Not a valid CSV file.")


