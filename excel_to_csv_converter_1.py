import pandas as pd
import os
import logging

def create_csv_files(input_excel_path, output_folder):
    if not os.path.exists(input_excel_path):
        logging.error(f"Input Excel file '{input_excel_path}' not found.")
        return

    try:
        df = pd.read_excel(input_excel_path)
    except Exception as e:
        logging.error(f"Error reading Excel file: {e}")
        return
    
    logging.info("Column names in the Excel file: %s", df.columns)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for index, row in df.iterrows():
        document_name = str(row['Document name'])
        csv_file_name = os.path.join(output_folder, f"{document_name}.csv")

        if os.path.exists(csv_file_name):
            csv_file_name = os.path.join(output_folder, f"{document_name}_{index}.csv")

        row_df = pd.DataFrame(row).T
        row_df.to_csv(csv_file_name, index=False, encoding='utf-8')

        logging.info("CSV file '%s' created.", csv_file_name)


logging.basicConfig(filename='csv_creation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

input_excel_path = input("Enter the path of the Excel file: ").strip()
output_folder = input("Enter the path of the output folder: ").strip()

create_csv_files(input_excel_path, output_folder)
