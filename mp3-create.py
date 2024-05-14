from gtts import gTTS
import os
from urllib.parse import urlparse

# Load environment variables from .env file
def load_env():
    env_vars = {}
    with open('.env', 'r') as file:
        for line in file:
            key, value = line.strip().split('=', 1)
            env_vars[key] = value
    return env_vars

# Load target URL from environment variables
env_vars = load_env()
url = env_vars.get('TARGET_URL')

if not url:
    print("Target URL not found in the .env file. Please set the TARGET_URL in the .env file.")
    exit()

# Define the path to the text file and the desired output audio folder
text_file_path = 'output/text_content.txt'
audio_folder = 'output/audio'

# Ensure the output audio folder exists or create it
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

# Extract the domain from the URL
domain = urlparse(url).netloc.split('.')[-2]  # Get the domain from the URL

# Read the text content from the file
with open(text_file_path, 'r', encoding='utf-8') as file:
    text_content = file.read()

# Create gTTS object to convert text content to speech
tts = gTTS(text=text_content, lang='en')

# Define the path for the output audio file with domain name
# Define the path for the output audio file as 'website.mp3'
audio_file_path = os.path.join(audio_folder, 'website.mp3')

# Save the converted text content to speech as an MP3 file with domain name
tts.save(audio_file_path)

print(f'Audio file saved successfully: {audio_file_path}')