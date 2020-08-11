# Import libraries
import pandas as pd
import numpy as np 
import os

# Change directory accordingly
os.chdir("C:\\Users\\nglee\\Desktop")

# Read dataset
df = pd.read_csv('dataset.csv')

# Delete any rows which do not have a name
df['name'].replace('', np.nan, inplace=True)
df.dropna(subset=['name'], inplace=True)

# Split the name field into first_name, and last_name
first_name_arr = []
last_name_arr = []
above_100_arr = []
for index, row in df.iterrows():
    name_arr = row['name'].split()
    for name_part in name_arr:
        # Remove salutations
        if "." in name_part:
            name_arr.remove(name_part)
        # Split into first and second names
        # Can ignore names at the end e.g. 'DDS', 'MD' since they are not important
    first_name_arr.append(name_arr[0])
    last_name_arr.append(name_arr[1])
    
    # Remove any zeros prepended to the price field
    price = float(str(row['price']).strip("0"))
    
    # Create a new field named above_100, which is true if the price is strictly greater than 100
    if (price > 100):
        above_100_arr.append(True)
    else:
        above_100_arr.append(False)

# Edit dataset
df['first_name'] = first_name_arr
df['last_name'] = last_name_arr
df['above_100'] = above_100_arr
df = df.drop('name', 1)

# Drop index so we don't export it
df = df.reset_index()
df = df.drop(['index'], axis=1)

# Export to csv
df.to_csv('new_dataset.csv', index=False)