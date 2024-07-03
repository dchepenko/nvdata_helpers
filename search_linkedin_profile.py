import serpapi
from serpapi import GoogleSearch

import csv

def search_linkedin_profiles(csv_file, name_col, company_col):
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        linkedin_links = []
        rows = list(reader)

    with open('updated_' + csv_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = reader.fieldnames + ['linkedin_profile']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in rows:
            name = row[name_col]
            company_domain = row[company_col]
            params = {
                "engine": "google",
                "q": f"{name}, {company_domain} linkedin.com",
                "api_key": "YOUR_API_KEY"
            }

            search = GoogleSearch(params)
            results = search.get_dict()
            profile_link = None

            for result in results.get("organic_results", []):
                link = result.get("link")
                if "linkedin.com/in/" in link:
                    profile_link = link
                    break

            row['linkedin_profile'] = profile_link
            writer.writerow(row)

    return 'updated_' + csv_file


search_linkedin_profiles('output_people.csv', 'full_name', 'domain')
