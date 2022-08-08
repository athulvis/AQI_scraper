# Import necessary packages
import pandas as pd
import camelot as camelot
from datetime import datetime

replace_string = datetime.today().strftime('%Y%m%d')
file = "https://cpcb.nic.in//upload/Downloads/AQI_Bulletin_20220307.pdf"
file = file.replace('20220307',str(replace_string),1)


# Extract tables 

tables = camelot.read_pdf(file, pages='all', strip_text='\n', flag_size=True)


# Define headers
def filter_df(df):
    df.columns = ['City', 'Air Quality', 'Index Value', 'Prominent Pollutant', 'No. of Monitoring Stations']
    df.reset_index().drop(columns= 'index', axis=1, inplace=True)
    return df

# Even number of dataframes
table_list = []
for num, table in enumerate(tables):
    if  num % 2 == 0:
        table_df = table.df
        table_list.append(table_df.drop(0).drop(0, axis=1))

# Concatenate all dateframes
df = pd.concat(table_list)

# Add headers
df.pipe(filter_df)

# Add date 
df['Date'] = pd.to_datetime('today').strftime("%d/%m/%Y")

# Append new data with old file
with open('AQI.csv', 'a') as f:
    df.to_csv(f, header=False, index=False)
