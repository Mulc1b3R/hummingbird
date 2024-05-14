import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

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
target_url = env_vars.get('TARGET_URL')

if not target_url:
    print("Target URL not found in the .env file. Please set the TARGET_URL in the .env file.")
    exit()

# Fetch the HTML content from the target URL
response = requests.get(target_url)
html_content = response.text

# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract all CSS file URLs from link tags in the HTML file
css_urls = [urljoin(target_url, link['href']) for link in soup.find_all('link', rel='stylesheet')]

# Create a directory to save the CSS files
output_dir = 'output/styles'
os.makedirs(output_dir, exist_ok=True)

# Download and save the CSS files
for idx, css_url in enumerate(css_urls, start=1):
    # Get the CSS file name from the URL
    css_name = os.path.basename(css_url)

    # Remove invalid characters from the CSS file name
    css_name = re.sub(r'[^\w\-_. ]', '', css_name)

    # Save the CSS file to the 'styles' directory
    css_path = os.path.join(output_dir, css_name)
    response = requests.get(css_url)

    with open(css_path, 'wb') as css_file:
        css_file.write(response.content)

    print(f'Saved CSS file {idx}: {css_name}')

print(f'All CSS files saved to {output_dir}')