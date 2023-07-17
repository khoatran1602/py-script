import csv
import sys

csv_file_path = sys.argv[1]

try:
    with open(csv_file_path, 'r') as file:
        dialect = csv.Sniffer().sniff(file.read(1024))
        if dialect.delimiter == ',':
            print("File format is valid: CSV")
        else:
            print("Invalid file format. Expected delimiter: ,")
except csv.Error:
    print("Invalid file format. Not a valid CSV file.")
