import pandas as pd

# Specify the file paths for the you need to check the duplicates CSV files
original_file = r'C:\Users\kanna\Downloads\s1.csv'

duplicate_file = r'C:\Users\kanna\Downloads\s2.csv'


# Read the Sheet1 data CSV file
original_data = pd.read_csv(original_file)

# Read the Sheet2 data CSV file
duplicate_data = pd.read_csv(duplicate_file)

# Replace 'Column_Name' with the actual column name you want to use for comparison, Colum should be same for both sheets
matches = pd.merge(duplicate_data, original_data, on='Serial Number', how='inner')

# Print the matching rows
print(matches)
