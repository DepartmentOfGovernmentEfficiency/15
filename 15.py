import requests
import pandas as pd

api_url = "https://api.usaspending.gov/api/v2/agency/015/awards/"

def fetch_awards_data():
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        print("Raw API Response:", data)
        return data.get("results", [])
    print("Error fetching data. Status code:", response.status_code)
    return []

data = fetch_awards_data()

contracts_data = []
for award in data:
    contracts_data.append({
        "Award Amount (USD)": "${:,.2f}".format(award.get("total_obligation", 0)),
        "Recipient": award.get("recipient", {}).get("name", "Unknown"),
        "Award Type": award.get("type", "Unknown"),
        "Award Date": award.get("date_signed", "Unknown"),
        "Award ID": award.get("id", "Unknown")
    })

if contracts_data:
    df = pd.DataFrame(contracts_data)
    print(df[["Award Amount (USD)"]])  
else:
    print("No data available from the awards API.")
