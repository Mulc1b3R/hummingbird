import os
import requests
from bs4 import BeautifulSoup

# Load environment variables from .env file
def load_env():
    env_vars = {}
    with open(".env", "r") as file:
        for line in file:
            line = line.strip()
            if '=' in line:
                key, value = line.split('=', 1)
                env_vars[key] = value
            else:
                print("Invalid line in .env file:", line)
    
    return env_vars  # Make sure to return the env_vars dictionary

# Load target URL from environment variables
env_vars = load_env()
url = env_vars.get('TARGET_URL')

if not url:
    print("Target URL not found in the .env file. Please set the TARGET_URL in the .env file.")
    exit()

# Function to extract and save text content from webpage
def save_text_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text content from the webpage
        text_content = ''
        for p_tag in soup.find_all('p'):
            text_content += p_tag.get_text() + '\n'

        # Save text content to a text file
        with open('output/text.txt', 'w', encoding='utf-8') as file:
            file.write(text_content)

        print('Text content saved to output/text_content.txt')
    else:
        print('Failed to retrieve webpage content')

# Extract and save text content from the target URL
save_text_content(url)