import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

# Function to clean up filename by replacing invalid characters
def clean_filename(filename):
    return re.sub(r'[^\w.-]', '_', filename)

# Read the target URL from the .env file
env_filename = '.env'
with open(env_filename, 'r') as env_file:
    for line in env_file:
        if line.strip():
            key, value = line.strip().split('=')
            if key == 'TARGET_URL':
                target_url = value
                break

# Fetch the HTML content from the target URL
response = requests.get(target_url)
html_content = response.text

# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract articles based on the specified HTML structure
articles = soup.find_all('div', class_='Article_hideOnDesktop__DU9kb')

# Store extracted article data in a list
article_data_list = []

for idx, article in enumerate(articles, start=1):
    article_title = urljoin(target_url, article.find('a')['href'])
    article_response = requests.get(article_title)
    article_html_content = article_response.text
    
    # Save the HTML content to an HTML file
    clean_article_title = clean_filename(os.path.basename(article_title)) + '.html'
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, clean_article_title), 'w', encoding='utf-8') as html_file:
        html_file.write(article_html_content)
        
    article_data_list.append({'title': article_title, 'html_file': clean_article_title})

# Generate an HTML file with clickable links to the articles
output_filename = 'articles_list.html'
output_dir = 'output'

with open(os.path.join(output_dir, output_filename), 'w') as html_file:
    html_file.write('<html><head><title>Articles List</title></head><body>')
    for idx, article_data in enumerate(article_data_list, start=1):
        html_file.write(f'<p><a href="{article_data["html_file"]}">Article {idx}</a>: {article_data["title"]}</p>')
    html_file.write('</body></html>')

print(f'HTML files saved in the "output" folder. Clickable links HTML file generated: {os.path.join(output_dir, output_filename)}')