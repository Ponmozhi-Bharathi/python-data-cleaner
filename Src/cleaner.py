import csv
import os
import argparse

from validators import (
    is_valid_name,
    is_valid_email,
    is_valid_phone
)

def clean_name(name):
    return name.strip().title()


def clean_email(email):
    return email.strip().lower()


def clean_city(city):
    return city.strip().title()


def clean_phone(phone):
    phone = phone.strip()

    if phone.startswith("+91"):
        phone = phone[3:]

    elif phone.startswith("91") and len(phone) == 12:
        phone = phone[2:]

    phone = phone.replace(" ", "")

    return phone


# Read CSV
def read_csv(filename):

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        print(f"❌ Error: File not found: {filename}")
        return []

    except PermissionError:
        print(f"❌ Error: Permission denied: {filename}")
        return []

    except UnicodeDecodeError:
        print(f"❌ Error: Unable to read file encoding: {filename}")
        return []


# Validate the Columns
def validate_columns(customers):

    required_columns = {
        "Name",
        "Email",
        "Phone",
        "City"
    }

    actual_columns = set(customers[0].keys())

    missing_columns = required_columns - actual_columns

    return missing_columns

# Find missing values
def find_missing_values(customers):

    missing_values = {}

    for customer in customers:

        for field, value in customer.items():

            if value.strip() == "":
                missing_values[field] = missing_values.get(field, 0) + 1

    return missing_values


# Clean data
def clean_data(customers):

    for customer in customers:
        customer["Name"] = clean_name(customer["Name"])
        customer["Email"] = clean_email(customer["Email"])
        customer["Phone"] = clean_phone(customer["Phone"])
        customer["City"] = clean_city(customer["City"])

    return customers


# Validate data

def validate_data(customers):

    valid_customers = []
    invalid_customers = []

    for customer in customers:

        name = customer["Name"]
        email = customer["Email"]
        phone = customer["Phone"]

        errors = []

        if name == "":
            errors.append("Missing Name")
        elif not is_valid_name(name):
            errors.append("Invalid Name")

        if email == "":
            errors.append("Missing Email")

        elif not is_valid_email(email):
            errors.append("Invalid Email")

        if phone == "":
            errors.append("Missing Phone")

        elif not is_valid_phone(phone):
            errors.append("Invalid Phone")

        if errors:

            customer["Reason"] = ", ".join(errors)
            invalid_customers.append(customer)

        else:

            valid_customers.append(customer)

    return valid_customers, invalid_customers


# Remove duplicates
def remove_duplicates(customers):

    unique_customers = []
    seen = set()

    for customer in customers:

        record = (
            customer["Name"],
            customer["Email"],
            customer["Phone"],
            customer["City"]
        )

        if record not in seen:

            seen.add(record)
            unique_customers.append(customer)

    return unique_customers



# Save Data

def save_csv(filename, customers, fieldnames):

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(customers)

def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Clean and validate customer CSV data."
    )

    parser.add_argument(
        "input_file",
        help="Path to the input CSV file"
    )

    parser.add_argument(
        "--output",
        default="output",
        help="Directory where output files will be saved"
    )

    return parser.parse_args()

def main():

    args = parse_arguments()

    #For Input 
    input_file = args.input_file

    if not input_file.lower().endswith(".csv"):
        print("❌ Error: Please provide a CSV file.")
        return

    filename = os.path.basename(input_file)
    name,  extension = os.path.splitext(filename)

    #For Output
    output_dir = args.output

    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(
        output_dir,
        f"cleaned_{name}.csv"
    )

    invalid_output_file = os.path.join(
        output_dir,
        f"invalid_{name}.csv"
    )

    report_file = os.path.join(
        output_dir,
        f"report_{name}.txt"
    )

    # Make sure output folder exists
    os.makedirs("output", exist_ok=True)

    # Read
    customers = read_csv(input_file)

    if not customers:
        print("❌ No data found. Please check the input CSV file.")
        return

    # Store original record count
    original_count = len(customers)

    # Validate the Columns
    missing_columns = validate_columns(customers)

    if missing_columns:
        print("❌ Error: Missing required columns:")
        
        for column in missing_columns:
            print(f"   - {column}")

        return
    print("Original records:", len(customers))

    # Missing values
    missing_values = find_missing_values(customers)

    # Clean
    customers = clean_data(customers)

    # Validate
    valid_customers, invalid_customers = validate_data(customers)

    # Remove duplicates
    unique_customers = remove_duplicates(valid_customers)

    # Save cleaned data
    save_csv(
        output_file,
        unique_customers,
        ["Name", "Email", "Phone", "City"]
    )

    # Save invalid data
    save_csv(
        invalid_output_file,
        invalid_customers,
        ["Name", "Email", "Phone", "City", "Reason"]
    )

    # Summary
    duplicates_removed = (
        len(valid_customers) - len(unique_customers)
    )

    # Generate cleaning report


    with open(report_file, "w", encoding="utf-8") as file:

        file.write("========================================\n")
        file.write("       CUSTOMER DATA CLEANING REPORT\n")
        file.write("========================================\n\n")

        file.write(f"Records processed: {original_count}\n\n")

        file.write("Missing values:\n")

        for field in ["Name", "Email", "Phone", "City"]:
            count = missing_values.get(field, 0)
            file.write(f"{field}: {count}\n")

        file.write("\nValidation:\n")
        file.write(f"Valid records: {len(valid_customers)}\n")
        file.write(f"Invalid records: {len(invalid_customers)}\n")

        file.write("\nDuplicates:\n")
        file.write(f"Duplicates removed: {duplicates_removed}\n")

        file.write(f"\nFinal clean records: {len(unique_customers)}\n")

        file.write("\nOutput files:\n")
        file.write("- output/cleaned_customers.csv\n")
        file.write("- output/invalid_customers.csv\n")
        file.write("- output/cleaning_report.txt\n")

        file.write("\n========================================\n")

    print("Report saved:", report_file)

if __name__ == "__main__":
    main()