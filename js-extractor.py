from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import re
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
target_url = env_vars.get('TARGET_URL')

if not target_url:
    print("Target URL not found in the .env file. Please set the TARGET_URL in the .env file.")
    exit()

# Fetch the HTML content from the target URL
response = requests.get(target_url)
html_content = response.text

# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract all JavaScript file URLs from script tags and external links in the HTML file
script_urls = []

# Extract script URLs from script tags
script_urls += [urljoin(target_url, script['src']) for script in soup.find_all('script') if script.get('src')]

# Extract external script URLs from links in the HTML head
head = soup.find('head')
if head:
    external_scripts = head.find_all('script', src=True)
    script_urls += [urljoin(target_url, script['src']) for script in external_scripts]

# Create a directory to save the JavaScript files
output_dir = 'output/js_files'
os.makedirs(output_dir, exist_ok=True)

# Download and save the JavaScript files
for idx, script_url in enumerate(script_urls, start=1):
    # Get the script file name from the URL
    script_name = os.path.basename(script_url)
    
    # Remove invalid characters from the script file name
    script_name = re.sub(r'[^\w\-_. ]', '', script_name)
    
    script_path = os.path.join(output_dir, script_name)
    response = requests.get(script_url)
    
    with open(script_path, 'wb') as script_file:
        script_file.write(response.content)
    
    print(f'Saved script {idx}: {script_name}')

print(f'All JavaScript files saved to {output_dir}')