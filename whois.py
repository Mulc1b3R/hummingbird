import whois
import json
from datetime import datetime
import os

# Load environment variables from .env file
def load_env():
    env_vars = {}
    with open('.env', 'r') as file:
        for line in file:
            key, value = line.strip().split('=', 1)
            env_vars[key] = value
    return env_vars

# Load target URL from environment variables
env_vars = load_env()
domain_name = env_vars.get('TARGET_URL')

if not domain_name:
    print("Target URL not found in the .env file. Please set the TARGET_URL in the .env file.")
    exit()

try:
    # Perform a 'whois' lookup for the target domain
    domain_info = whois.whois(domain_name)

    # Convert datetime object to string
    def default(o):
        if isinstance(o, datetime):
            return o.isoformat()

    # Create a dictionary with the 'whois' data
    website_data = {
        "domain_name": domain_name,
        "whois_info": domain_info,
        "timestamp": datetime.now()
    }

    # Serialize the dictionary to JSON with datetime formatting
    output_file = "output/whois_info.json"
    with open(output_file, "w") as file:
        json.dump(website_data, file, default=default, indent=4)

    print(f"Whois information saved to {output_file}")

except whois.parser.PywhoisError as e:
    print(f"An error occurred during 'whois' lookup: {e}")

except Exception as e:
    print(f"An error occurred: {e}")