import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Function to save external links as a list in an HTML file
def save_external_links_html(file_path, links):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('<html>\n<head>\n<title>External Links</title>\n</head>\n<body>\n')
        file.write('<h1>List of External Links:</h1>\n')
        file.write('<ul>\n')
        
        for link in links:
            file.write(f'<li><a href="{link}">{link}</a></li>\n')
        
        file.write('</ul>\n')
        file.write('</body>\n</html>')

# Read the target URL from the .env file
env_file_path = ".env"
target_url = ''

with open(env_file_path, 'r') as env_file:
    for line in env_file:
        if line.strip():
            key, value = line.strip().split('=')
            if key == 'TARGET_URL':
                target_url = value
                break

if not target_url:
    print("Error: TARGET_URL not found in the .env file.")
    exit()

# Extract external links
response = requests.get(target_url)
soup = BeautifulSoup(response.text, 'html.parser')

external_links = []
for link in soup.find_all('a', href=True):
    href = link.get('href')
    if href and 'http' in href and urlparse(target_url).netloc not in href:
        external_links.append(urljoin(response.url, href))

# Save the list of external links as an HTML file
output_folder = 'output'
output_file_path = os.path.join(output_folder, 'ex-links.html')

save_external_links_html(output_file_path, external_links)