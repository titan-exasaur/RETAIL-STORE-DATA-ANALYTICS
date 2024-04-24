import os
directory = r'/media/kumar/HDD1/INFIDATA/INFIDATA PROJECTS/OCT-DEC RBITS PROJECTS/29 [REVA] RETAIL STORE DATA ANALYTICS/data'
# print(os.listdir(directory))

# Iterate over the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.CSV'):
        # Extract month and year from the filename
        parts = filename.split('_')
        month_year = parts[-1].split('.')[0]
        print(f"Month_year: {month_year}")
        month = ''
        year = ''
        for char in month_year:
            if char.isdigit():
                year += char
            else:
                month += char
        # Create the new filename
        new_filename = f"{month}_{year}.csv"
        
        # Construct the full paths for the old and new filenames
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed {filename} to {new_filename}")
