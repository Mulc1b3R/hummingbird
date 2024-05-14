

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

# Function to clean up filename by replacing invalid characters
def clean_filename(filename):
    return re.sub(r'[^\w.-]', '_', filename)

# Read the target URL from the .env file
with open('.env', 'r') as env_file:
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

for article in articles:
    article_title = urljoin(target_url, article.find('a')['href'])
    
    img_tag = article.find('img')
    if img_tag:
        article_img = urljoin(target_url, img_tag.get('src'))
        
        # Save the image to the 'img' folder
        img_response = requests.get(article_img)
        img_filename = clean_filename(os.path.basename(article_img))
        
        img_dir = 'output/img'
        os.makedirs(img_dir, exist_ok=True)
        
        with open(os.path.join(img_dir, img_filename), 'wb') as img_file:
            img_file.write(img_response.content)
        
    else:
        article_img = 'No image found'
        
    article_data_list.append({'title': article_title, 'image': article_img})

# Generate HTML content for template3.html
html_content = '<div style="display: grid; place-items: center; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px;">'
for idx, article_data in enumerate(article_data_list, start=1):
    html_content += f'<div><a href="{article_data["title"]}"><img src="{article_data["image"]}" alt="Article Image"></a></div>'
html_content += '</div>'

# Write the HTML content to template3.html
output_filename = 'template3.html'
output_dir = 'output'

os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, output_filename), 'w') as html_file:
    html_file.write(html_content)

print(f'HTML content with images and links arranged in a grid stored in: {output_dir}/{output_filename}')
print(f'All JPG images saved to the "img" folder.')