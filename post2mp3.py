import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
from gtts import gTTS

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
    
    # Save the HTML content to a TXT file
    clean_article_title = clean_filename(os.path.basename(article_title)) + '.txt'
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, clean_article_title), 'w', encoding='utf-8') as txt_file:
        # Extract text content from HTML and save to TXT file
        soup_article = BeautifulSoup(article_html_content, 'html.parser')
        text_content = ' '.join([p.get_text() for p in soup_article.find_all('p')])
        txt_file.write(text_content)
        
    article_data_list.append({'title': article_title, 'txt_file': clean_article_title})

# Convert the TXT files to MP3 files using gTTS
audio_dir = os.path.join('output', 'audio')
os.makedirs(audio_dir, exist_ok=True)

for idx, article_data in enumerate(article_data_list, start=1):
    with open(os.path.join(output_dir, article_data['txt_file']), 'r', encoding='utf-8') as txt_file:
        text_data = txt_file.read()
        tts = gTTS(text=text_data, lang='en', slow=False)
        tts.save(os.path.join(audio_dir, f'article_{idx}.mp3'))

print(f'TXT files saved in the "output" folder. MP3 files generated in the "audio" folder.')