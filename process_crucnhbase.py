import csv
import re
import requests


def process_people_from_csv(input_csv, output_csv, people_column_name, organization_column_name):
    with open(input_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames

        # Prepare to write to output CSV
        with open(output_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['full_name', 'domain'])
            # Write header for output CSV with an additional column for linking

            for row in reader:
                people = row[people_column_name]
                organization_key = extract_domain(row[organization_column_name])
                individuals = people.split(',')
                for individual in individuals:
                    writer.writerow([individual.strip(), organization_key])  
                    # Write each person to the output CSV along with the organization key


# Example usage:
process_people_from_csv('startup.csv', 'output_people.csv', 'Founders', 'Website')

