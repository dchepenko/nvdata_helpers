# Helper function that are used in various ad-hoc tasks

## Description
- `process_crucnhbase.py` 
Extracts founders' names and their associated company domains from a given CSV file of Crunchbase company export

- `search_linkedin_profile.py`
The script reads a CSV file containing candidate data with a Full Name and Organization Name. 
Automatically searches for LinkedIn profiles using this data using `SERP API`

- `search_linkedin_profile.py`
The script reads a CSV file containing candidate data with a LinkedIn profiles and other relevant information. 
Each candidate's data is sent to the SignalHire API. If the API request is successful, the script outputs a success message along with the response data. If the request fails, it outputs an error message detailing the issue.

## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file. You can find a template for these variables in the `.env.example` file included in the repository.

- `SIGNALHIRE_API_KEY`
  - Description: This is the API key used to authenticate requests to the SignalHire API.
  - Required: Yes
  - How to Obtain: You can obtain this key by registering or logging into your SignalHire account and accessing the API section.

- `CALLBACK_URL`
  - Description: The URL to which SignalHire will send responses after processing your requests.
  - Required: Yes
  - Example: `https://yourdomain.com/callback`

- `SERP_API_KEY`
  - Description: This key is used to authenticate requests to the SERP API for performing searches.
  - Required: Yes
  - How to Obtain: Register on the SERP API's website to receive an API key.

### Setting Up Your `.env` File
1. Create a file named `.env` in the root directory of your project.
2. Replace the placeholder values with your actual data.
