import requests
from bs4 import BeautifulSoup
import os
import configparser

def extract_favicon(target_url):
    response = requests.get(target_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    icon_urls = set()
    for meta_tag in soup.find_all('link', rel=['icon', 'shortcut icon']):
        icon_url = meta_tag.get('href')
        if icon_url:
            icon_urls.add(icon_url if icon_url.startswith('http') else target_url + icon_url)
    
    icons_dir = 'output/img'
    os.makedirs(icons_dir, exist_ok=True)
    
    img_paths = []
    for idx, icon_url in enumerate(icon_urls, start=1):
        response = requests.get(icon_url)
        icon_path = os.path.join(icons_dir, f'favicon_{idx}.png')
        
        with open(icon_path, 'wb') as icon_file:
            icon_file.write(response.content)
        
        img_paths.append(icon_path)
    
    return img_paths

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

favicons = extract_favicon(target_url)

for idx, favicon in enumerate(favicons, start=1):
    print(f'Favicon {idx} saved: {favicon}')