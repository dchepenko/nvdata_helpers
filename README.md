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

To get the response the 