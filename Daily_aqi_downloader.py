from datetime import datetime, timedelta
import os
import requests
import pandas as pd

# Date
today = datetime.today()
date_str = today.strftime("%Y%m%d")

# Functions

def download_file(date_str):
    """
    Download AQI Bulletin PDF file for a specific date.
    """
    file_url = f"https://cpcb.nic.in//upload/Downloads/AQI_Bulletin_{date_str}.pdf"
    filename = f"AQI_Bulletin_{date_str}.pdf"
    response = requests.get(file_url)
    
    with open(os.path.join("data/", filename), "wb") as f:
        f.write(response.content)

# Download files
download_file(date_str)

