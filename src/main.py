# Main code
import requests
import json

# URL for the Tomorrow.io Weather Forecast API
url = "https://api.tomorrow.io/v4/weather/forecast?location=orebro&timesteps=1d&units=metric&apikey=nukb3RL1iHdl4Pp4o0j58ONKsbRoVMxr"

headers = {"accept": "application/json"}

# Send the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Print each key-value pair in the response
    for day in data.get('timelines', {}).get('daily', []):
        for key, value in day.items():
            print(f"{key}: {value}")
        print("\n---\n")  # Separate each day's data
else:
    print(f"HTTP Error: {response.status_code}")
