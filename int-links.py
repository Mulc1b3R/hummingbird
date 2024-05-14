import os
from bs4 import BeautifulSoup
import shutil
import requests

# Base URL
TARGET_URL = 'https://classiccinemaonline.com/'  # Update with your actual base URL

# Define headers for the request
headers = {"csrf.token":"1e0be4b3964f01115c65679524f3a7a7","system.paths":{"root":"","base":""}
}

# Path to the input HTML file
input_file_path = 'output/index.html'
# Path to the output folder
output_folder = 'output'

# Create a list to store internal links
internal_links = []

# Read the input HTML file
with open(input_file_path, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all internal link elements using BeautifulSoup
for link in soup.find_all('a'):
    href = link.get('href')
    if href and not href.startswith('http'):
        internal_links.append(href)

# Write the internal links to a file called 'links.html'
with open(os.path.join(output_folder, 'int-links.html'), 'w') as links_file:
    links_file.write('\n'.join(internal_links))

# Copy all linked pages to the 'output' folder
for link in internal_links:
    page_name = link.replace('/', '_') + ".html"  # Modify page name to prevent clashes
    source = TARGET_URL + link
    destination = os.path.join(output_folder, page_name)
    
    # Fetch the file using requests with custom headers
    response = requests.get(source, headers=headers)
    
    if response.status_code == 200:
        with open(destination, 'wb') as output_file:
            output_file.write(response.content)
        print(f"Copied {source} to {destination}")
    else:
        print(f"Failed to fetch {source}. Status code: {response.status_code}")

print("Linked pages copied successfully!")