# 📁 Python Data Cleaner

A Python command-line tool that cleans, validates, and processes customer data stored in CSV files.

##  🛠️ Features

* Read customer data from CSV files
* Detect missing values
* Clean and normalize names
* Clean and normalize email addresses
* Normalize Indian phone numbers
* Validate names, emails, and phone numbers
* Separate valid and invalid records
* Remove duplicate records
* Save cleaned data to a CSV file
* Save invalid records with the reason for failure
* Generate a cleaning report
* Handle missing files and invalid input
* Support custom output directories

##  📂 Technologies

* Python
* CSV
* Regular Expressions
* argparse
* Git
* GitHub

## Project Structure

```text
python-data-cleaner/
│
├── Data/
│   └── customers.csv
│
├── Src/
│   ├── cleaner.py
│   └── validators.py
│
├── output/
│   ├── cleaned_customers.csv
│   ├── invalid_customers.csv
│   └── report_customers.txt
│
├── .gitignore
├── README.md
└── requirements.txt
```

## ⚙️ Requirements

* Python 3.x
* Git

The project currently uses Python's standard library, so no external Python packages are required.

## ▶️ How to Run

Open the terminal in the project folder and run:

```bash
python Src/cleaner.py Data/customers.csv
```

The program will clean and validate the customer data.

## 📁 Custom Output Directory

You can choose where the generated files are saved:

```bash
python Src/cleaner.py Data/customers.csv --output results
```

## 📊 Output Files

The program generates:

### Cleaned Data

`cleaned_customers.csv`

Contains valid records after cleaning and duplicate removal.

### Invalid Data

`invalid_customers.csv`

Contains records that failed validation and the reason they were rejected.

### Cleaning Report

`report_customers.txt`

Contains a summary of the cleaning process, including:

* Records processed
* Missing values
* Valid records
* Invalid records
* Duplicates removed
* Final clean records

## 🧹 Data Cleaning Process

```text
Input CSV
    ↓
Read Data
    ↓
Check Required Columns
    ↓
Detect Missing Values
    ↓
Clean and Normalize Data
    ↓
Validate Data
    ↓
Separate Valid and Invalid Records
    ↓
Remove Duplicates
    ↓
Save Cleaned Data
    ↓
Save Invalid Data
    ↓
Generate Report
```

💡 Example

Run:
```bash
python Src/cleaner.py Data/customers.csv
```

The program processes the CSV and produces:

Records processed:   50000
Valid records:       ...
Invalid records:     ...
Duplicates removed:  ...
Clean records:       ...

Output files:
output/cleaned_customers.csv
output/invalid_customers.csv
output/report_customers.txt

## Purpose

This project demonstrates practical Python skills including:

* File handling
* CSV processing
* Data cleaning
* Data validation
* Regular expressions
* Functions
* Modular programming
* Error handling
* Command-line applications

## Author

Ponmozhi-Bharathi
