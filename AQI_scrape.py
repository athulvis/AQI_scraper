# Import necessary packages
import pandas as pd
import camelot
from datetime import datetime
import cv2

# Date
today = datetime.today()
date_str = today.strftime("%Y%m%d")

file = f'data/AQI_Bulletin_{date_str}.pdf'

#file = f'data/AQI_Bulletin_20231217.pdf'
# Extract tables 
tables = camelot.read_pdf(file, pages='all', strip_text='\n', flag_size=True)

# Define headers
def filter_df(df):
    df.columns = ['City', 'Air Quality', 'Index Value', 'Prominent Pollutant', 'No. of Monitoring Stations']
    df.reset_index(drop=True, inplace=True)
    return df

# Even number of dataframes
table_list = []
for num, table in enumerate(tables):
    if num % 2 == 0:
        table_df = table.df
        table_list.append(table_df.drop(0).drop(0, axis=1, inplace=True))

# Concatenate all dataframes
df = pd.concat(table_list)

# Add headers
df = df.pipe(filter_df)

# Add date 
df['Date'] = date_str

# Append new data with old file
with open('AQI.csv', 'a') as f:
    df.to_csv(f, header=False, index=False)

