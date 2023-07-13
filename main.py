import csv
import sys
from collections import namedtuple
from datetime import datetime

def validate_name(name):
    return len(name) <= 50

def validate_married(married):
    return married.lower() in {'Y', 'N'}

def validate_gender(gender):
    return gender in {'M', 'F'}

def validate_identification_number(identification_number):
    return identification_number.isdigit() and len(identification_number) == 10

def validate_row(row):
    return all([
        validate_name(row.name),
        validate_married(row.married),
        validate_gender(row.gender),
        validate_identification_number(row.id_number)
    ])

def process_csv(file_path):
    with open(file_path, 'r') as csvfile:
        fieldnames = ['name', 'married', 'gender', 'dob', 'id_number']
        Data = namedtuple('Data', fieldnames)
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)

        # Skip the header (first row)
        next(reader)

        result_map = {}
        duplicated_rows = []

        for row in reader:
            data = Data(**row)
            if validate_row(data):
                if data.name in result_map:
                    duplicated_rows.append(data)
                else:
                    result_map[data.name] = (data.married, data.gender, data.dob, data.id_number)
            else:
                print(f"Invalid row: {row}")

        # Remove duplicated rows from result_map
        for duplicate in duplicated_rows:
            if duplicate.name in result_map:
                del result_map[duplicate.name]

    return result_map, duplicated_rows

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 validation.py input.csv")
        sys.exit(1)

    file_path = sys.argv[1]
    valid_data_map, duplicated_rows = process_csv(file_path)
    print(len(duplicated_rows))