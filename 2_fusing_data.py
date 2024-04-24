import os
import pandas as pd

def merge_monthly_data(directory:str) -> pd.DataFrame:
    merged_data = None  # Initialize merged_data as None
    
    for file in os.listdir(directory):
        if file.endswith('.csv'):
            file_path = os.path.join(directory, file)
            month_year = file.split('.')[0]  # Extract month and year from filename
            if '_' in month_year:  # Ensure that month_year contains an underscore
                month, year = month_year.split('_')  # Split the filename into month and year
                
                # Load CSV into DataFrame
                df = pd.read_csv(file_path)
                
                # Extract existing column names
                columns = df.columns.tolist()
                # Assume the columns containing quantity and amount have names containing these strings
                quantity_column = [col for col in columns if 'quantity' in col.lower()][0]
                amount_column = [col for col in columns if 'amount' in col.lower()][0]
                
                # Rename columns to include month and year
                df.rename(columns={quantity_column: f'{month}_{year}_quantity',
                                   amount_column: f'{month}_{year}_amount'}, inplace=True)
                
                # Merge with main DataFrame based on product_name, filling missing values with zeros
                if merged_data is None:
                    merged_data = df.copy()  # If merged_data is None, assign the first DataFrame directly
                else:
                    merged_data = pd.merge(merged_data, df, on='product_name', how='outer').fillna(0)
    
    return merged_data

# Directory containing monthly CSV files
data_directory = "/media/kumar/HDD1/INFIDATA/INFIDATA PROJECTS/OCT-DEC RBITS PROJECTS/29 [REVA] RETAIL STORE DATA ANALYTICS/cleaned_data"

# Merge monthly data
merged_data = merge_monthly_data(data_directory)

# Save merged data to a new CSV file
merged_data.to_csv("/media/kumar/HDD1/INFIDATA/INFIDATA PROJECTS/OCT-DEC RBITS PROJECTS/29 [REVA] RETAIL STORE DATA ANALYTICS/merged_data.csv", index=False)

# Display the merged DataFrame
print(merged_data.head())

