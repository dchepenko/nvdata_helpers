import csv
import os
import sys

import serpapi
from serpapi import GoogleSearch

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
                "api_key": os.getenv('SERP_API_KEY')
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

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Search LinkedIn profiles based on names and company domains from a CSV file.")
    parser.add_argument("csv_file", type=str, help="Path to the input CSV file.")
    parser.add_argument("--name_column", type=str, default='full_name', help="Column name for candidate names. Default is 'full_name'.")
    parser.add_argument("--company_column", type=str, default='domain', help="Column name for company domains. Default is 'domain'.")
    args = parser.parse_args()

    search_linkedin_profiles(args.csv_file, args.name_column, args.company_column)


git filter-branch --force --index-filter \
"git rm --cached --ignore-unmatch path/to/file" \
--prune-empty --tag-name-filter cat -- --all