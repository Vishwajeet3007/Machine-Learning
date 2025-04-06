import requests
from io import StringIO
import pandas as pd

# Replace with the actual CSV file URL
url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

# Optional headers (use if required)
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Requesting the CSV file
req = requests.get(url, headers=headers)

# Check if the request was successful
if req.status_code == 200:
    data = StringIO(req.text)  # Convert response text into file-like object
    df = pd.read_csv(data)  # Read CSV into Pandas DataFrame
    print(df.head())  # Display first few rows
else:
    print(f"Failed to fetch data. Status Code: {req.status_code}")

