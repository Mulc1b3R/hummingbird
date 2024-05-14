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

# List of file extensions to look for
file_types = ["pdf","zip" "doc", "docx", "xml", "htm", "xls", "xlsx"]

# Function to filter links by file type
def filter_links(link, file_types):
    for file_type in file_types:
        if re.search(fr'\.{file_type}$', link, re.IGNORECASE):
            return True
    return False

# Find all links with specified file types
download_urls = []
for link in soup.find_all("a", href=True):
    href = link["href"]
    if filter_links(href, file_types):
        download_urls.append(href)

# Create a directory to save downloaded files
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Download the specified files
for index, url in enumerate(download_urls, start=1):
    file_name = f"file_{index}.{url.split('.')[-1]}"
    output_path = os.path.join(output_dir, file_name)
    with open(output_path, "wb") as file:
        file_response = requests.get(url)
        file.write(file_response.content)
        print(f"Downloaded: {url} -> {output_path}")