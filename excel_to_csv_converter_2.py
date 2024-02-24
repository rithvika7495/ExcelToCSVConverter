import pandas as pd
import os
import argparse
import logging

def process_excel_to_csv(excel_file_path, output_dir):

    df = pd.read_excel(excel_file_path)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logging.info(f'Created output directory: {output_dir}')

    for document_name in df['Document Name'].unique():
        subset_df = df[df['Document Name'] == document_name]

        output_csv_path = os.path.join(output_dir, f'{document_name}.csv')

        if os.path.exists(output_csv_path):
            logging.warning(f'CSV file "{output_csv_path}" already exists and will be overwritten.')

        subset_df.to_csv(output_csv_path, index=False, encoding='utf-8')

        logging.info(f'CSV file "{output_csv_path}" created.')

def main():
    logging.basicConfig(filename='data_processing.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    parser = argparse.ArgumentParser(description='Process Excel file to CSV files')
    parser.add_argument('excel_file', type=str, help='Path to the input Excel file')
    parser.add_argument('output_dir', type=str, help='Path to the output directory for CSV files')
    args = parser.parse_args()

    process_excel_to_csv(args.excel_file, args.output_dir)

if __name__ == '__main__':
    main()
