# Excel to CSV Converter

📄 🔄 ➡️ 🗃️

This repository contains a Python script that converts data from an Excel file to CSV files. Each row in the Excel file is converted into a separate CSV file. The script prompts the user to input the path of the Excel file and the output folder where the CSV files will be saved. It utilizes the pandas library for reading Excel files and managing data. Additionally, logging is implemented to track the script's activities. This tool provides a convenient way to convert Excel data into a more portable and widely supported format, suitable for various data processing tasks.

## Prerequisites

- Python 3.x
- pandas library

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/rithvika7495/excel-to-csv-converter.git
    ```

2. Install the required dependencies:

    ```bash
    pip install pandas
    ```

## Usage

1. Run the script `convert_excel_to_csv.py`.

2. You will be prompted to enter the path of the Excel file and the output folder.

3. Once you provide the paths, the script will convert each row of the Excel file into a separate CSV file and save them in the specified output folder.

## Example

Suppose you have an Excel file named `data.xlsx` with the following content:

| Document name | Content |
|---------------|---------|
| Document1     | Content1|
| Document2     | Content2|

Running the script and providing the paths, the output folder will contain two CSV files:

- `Document1.csv` with content "Content1"
- `Document2.csv` with content "Content2"

## Logging

The script logs its activities to a file named `csv_creation.log` for better tracking.
