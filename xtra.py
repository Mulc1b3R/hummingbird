import os
import requests
from bs4 import BeautifulSoup
import os
import requests
from bs4 import BeautifulSoup

# Read .env file and set environment variables
with open('.env', 'r') as f:
    for line in f:
        key, value = line.strip().split('=')
        os.environ[key] = value

# Function to download files
def download_file(url, output_dir):
    response = requests.get(url)
    if response.status_code == 200:
        filename = url.split('/')[-1]
        with open(os.path.join(output_dir, filename), 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {filename}")

# Load HTML content from the target URL
target_url = os.getenv("TARGET_URL")
response = requests.get(target_url)
html_content = response.text

# Parse HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find and download resources of type manifest, font, and RSS links
for link in soup.head.find_all('link'):
    link_type = link.get('rel')
    if link_type:
        if 'manifest' in link_type:
            manifest_url = link.get('href')
            if manifest_url:
                download_file(manifest_url, 'output')

        if 'stylesheet' in link_type:
            font_url = link.get('href')
            if font_url and ('font' in font_url or 'fonts' in font_url):
                download_file(font_url, 'output')

        if 'alternate' in link_type:
            if link.get('type') == 'application/rss+xml':
                rss_url = link.get('href')
                if rss_url:
                    download_file(rss_url, 'output')