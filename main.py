from collections import namedtuple
import csv
import sys


def validate_name(name):
    if len(name) > 50:
        return False, "Invalid name"
    return True, ""

def validate_married(married):
    if married.lower() not in {'true', 'false'}:
        return False, "Invalid married status"
    return True, ""

def validate_gender(gender):
    if gender not in {'M', 'F'}:
        return False, "Invalid gender"
    return True, ""

def validate_identification_number(identification_number):
    if not identification_number.isdigit() or len(identification_number) != 10:
        return False, "Invalid identification number"
    return True, ""

def validate_row(row):
    errors = []
    for validator in [validate_name, validate_married, validate_gender, validate_identification_number]:
        valid, error = validator(getattr(row, validator.__name__))
        if not valid:
            errors.append(error)
    return len(errors) == 0, errors

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
            is_valid, errors = validate_row(data)

            if is_valid:
                # Convert all fields to strings except 'id_number' and remove 'dob'
                converted_data = {
                    'name': str(data.name),
                    'married': str(data.married),
                    'gender': str(data.gender),
                    'id_number': int(data.id_number)
                }

                if data.name in result_map:
                    duplicated_rows.append(converted_data)
                else:
                    result_map[data.name] = converted_data
            else:
                print(f"Invalid row: {row} - Errors: {', '.join(errors)}")

    return result_map, duplicated_rows

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 validation.py input.csv")
        sys.exit(1)

    file_path = sys.argv[1]
    valid_data_map, duplicated_rows = process_csv(file_path)
    print("Valid data map:")
    for key, value in valid_data_map.items():
        print(f"{key}: {value}")

    print("\nDuplicated rows:")
    for row in duplicated_rows:
        print(row)