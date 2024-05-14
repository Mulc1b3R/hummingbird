import requests
from bs4 import BeautifulSoup
import re
import os

# Function to read values from .env file
def read_from_env(file_path):
    with open(file_path) as file:
        env_variables = {}
        for line in file:
            key, value = line.strip().split('=')
            env_variables[key] = value
        return env_variables

# Read target URL from .env file
env_vars = read_from_env(".env")
target_url = env_vars.get("TARGET_URL")

# Send a GET request and parse the HTML content
response = requests.get(target_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all embedded objects with SWF files
swf_urls = []
for embed in soup.find_all('embed', type='application/x-shockwave-flash'):
    swf_url = embed.get('src')
    if swf_url:
        swf_urls.append(swf_url)

# Find all SWF files linked in anchor tags
for a in soup.find_all('a', href=True):
    if re.search(r'\.swf$', a['href']):
        swf_urls.append(a['href'])

# Create a directory to save downloaded SWF files
if not os.path.exists("output/downloaded_swf_files"):
    os.makedirs("output/downloaded_swf_files")

# Download the SWF files
for index, url in enumerate(swf_urls):
    filename = f"downloaded_swf_files/swf_file_{index + 1}.swf"
    with open(filename, 'wb') as file:
        response = requests.get(url)
        file.write(response.content)
        print(f"Downloaded: {url} -> {filename}")