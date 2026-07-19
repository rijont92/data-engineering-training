# Day 2 Practice - CSV Mini Data Pipeline

This project reads raw student data from a CSV file, checks data quality issues, cleans the data using Python, saves a cleaned CSV file, and generates summary reports.

The goal of this practice is to understand how raw data is transformed into clean and useful data through a simple data pipeline process.

## Input

- data/students_raw.csv

The input file contains raw student records with missing values, inconsistent text formatting, and invalid numeric values that need to be cleaned.

## Outputs

Generated files are saved inside the output folder:

- output/students_clean.csv
- output/data_quality_report.txt
- output/summary_report.txt

## How to run

Run the pipeline from the day-2-practice folder:

```bash
python csv_pipeline.py

The program will:

Read the raw CSV file.
Inspect records and columns.
Detect data quality issues.
Clean and transform student data.
Generate cleaned CSV output.
Create data quality and summary reports.
Concepts practiced
CSV files
Reading and writing files with Python
Lists and dictionaries
Loops and conditions
Functions
Data cleaning and validation
Data transformation
Generating reports
Error handling
GitHub project organization
Bonus features added
Attendance level classification:
High
Medium
Low
Average attendance by course report section
Average homework score by city report section
Duplicate student ID detection
Automatic output folder creation
Basic file error handling

Project Structure
day-2-practice/
│
├── csv_pipeline.py
├── README.md
├── daily_report.txt
│
├── data/
│   └── students_raw.csv
│
└── output/
    ├── students_clean.csv
    ├── data_quality_report.txt
    └── summary_report.txt