#LOADING NECESSARY PACKAGES
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print('[info] all necessary packages imported successfully...')

def load_data(csv_path):
    dataframe = pd.read_csv(rf'{csv_path}')
    return dataframe

# data = load_data("/media/kumar/HDD1/INFIDATA/INFIDATA PROJECTS/OCT-DEC RBITS PROJECTS/29 [REVA] RETAIL STORE DATA ANALYTICS/data/JAN_23.csv")

def clean_data(dataframe_input):
    dataframe_input = dataframe_input.drop([0, 1, 2, 3, 4])# Dropping rows 0, 1, 2, 3 and 4
    dataframe_input = dataframe_input.reset_index(drop=True)# Resetting indexes
    dataframe_input.columns = ['product_name','quantity','amount']

    dataframe_input = dataframe_input.dropna()
    dataframe_input = dataframe_input.reset_index(drop=True)

    cleansed_data = dataframe_input
    return cleansed_data

# clean_data = clean_data(data)
# print(clean_data.columns[clean_data.isna().any()])


def process_files(input_dir, output_dir):
    # Get list of files in the input directory
    files = os.listdir(input_dir)
    
    for file in files:
        if file.endswith('.csv'):  # Assuming all files have CSV extension
            file_path = os.path.join(input_dir, file)
            print(f"Processing file: {file_path}")
            
            # Load data
            data = load_data(file_path)
            
            # Clean data
            clean_data_df = clean_data(data)
            
            # Save cleaned data
            output_file_path = os.path.join(output_dir, f"{file}")
            clean_data_df.to_csv(output_file_path, index=False)
            print(f"Cleaned data saved to: {output_file_path}")

# Input and output directories
input_directory = "/media/kumar/HDD1/INFIDATA/INFIDATA PROJECTS/OCT-DEC RBITS PROJECTS/29 [REVA] RETAIL STORE DATA ANALYTICS/data/"
output_directory = "/media/kumar/HDD1/INFIDATA/INFIDATA PROJECTS/OCT-DEC RBITS PROJECTS/29 [REVA] RETAIL STORE DATA ANALYTICS/cleaned_data/"

# Process files
process_files(input_directory, output_directory)

