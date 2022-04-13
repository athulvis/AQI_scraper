# Import necessary packages
import camelot as camelot
import pandas as pd

# Extract tables 
file = "https://cpcb.nic.in//upload/Downloads/AQI_Bulletin_20220307.pdf"
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
df



# load previous data
df_base = pd.read_csv("AQI.csv")
#df_base["Date"] = pd.to_datetime(df_base["Date"], format="%d/%m/%Y")


# Append latest data
frames = [df, df_base]
df1 = pd.concat(frames)

#dates
#df1["Date"] = pd.to_datetime(df1["Date"], format="%d/%m/%Y")

# Remove duplicate rows
df1.drop_duplicates(keep=False)

# Export to csv
df1.to_csv("AQI.csv",index = False)
df1

#dataTypeSeries = df1.dtypes

#print(dataTypeSeries)