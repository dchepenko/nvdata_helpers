import csv
import re
import sys
import argparse


def extract_domain(url):
    # Regex pattern to extract the domain from a URL
    pattern = r"^(?:https?:\/\/)?(?:www\.)?([^\/]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return "unknown"  # Return a default value if no domain is found


def process_people_from_csv(input_csv, output_csv):
    with open(input_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        # Prepare to write to output CSV
        with open(output_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['full_name', 'domain'])
            # Write header for output CSV with an additional column for linking

            for row in reader:
                people = row["Founders"]
                organization_key = extract_domain(row["Website"])
                individuals = people.split(',')
                for individual in individuals:
                    writer.writerow([individual.strip(), organization_key])  
                    # Write each person to the output CSV along with the organization key


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Crunchbase CSV to extract people and their domains.")
    parser.add_argument("input_csv", type=str, help="Input CSV file path")
    parser.add_argument("output_csv", type=str, help="Output CSV file path")
    args = parser.parse_args()

    process_people_from_csv(args.input_csv, args.output_csv)
