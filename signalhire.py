import json
import requests
import argparse
import os

from itertools import islice


API_KEY = os.getenv('SIGNALHIRE_API_KEY')
CALLBACK_URL = os.getenv('CALLBACK_URL')

import csv

# Endpoint URL
url = 'https://www.signalhire.com/api/v1/candidate/search'

# Request headers
headers = {
    'apikey': API_KEY,
    'Content-Type': 'application/json'
}

def send_candidate_data(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)

        for row in islice(reader, 6, 55):
            linkedin_profile = row.get('linkedin_profile', None)
            if linkedin_profile != None:
                # Request body
                data = {
                    'items': [
                        linkedin_profile  # Provide a default value if key is missing
                    ],
                    'callbackUrl': CALLBACK_URL
                }

                # Convert data to JSON string
                json_data = json.dumps(data)

                # Make the API request
                response = requests.post(url, headers=headers, data=json_data)

                # Check if the request was successful (status code 201)
                if response.status_code == 201:
                    responseData = response.json()
                    print(f"Request for {row['full_name']} successful: {responseData}")
                else:
                    print(f"Error for {row['full_name']}: {response.status_code}, {response.text}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send candidate data to SignalHire API.")
    parser.add_argument("input_csv", type=str, help="Path to the input CSV file containing candidate data.")
    args = parser.parse_args()

    send_candidate_data(args.input_csv)
