import requests
from bs4 import BeautifulSoup
import os

def extract_media_files(download_folder):
    target_url = 'https://www.gamespot.com/videos/fortnite-x-avatar-elements-gameplay-trailer/2300-6463878/'
    
    response = requests.get(target_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for link in soup.find_all('a'):
            if link.get('href'):
                href = link.get('href')
                if href.endswith('.mp3') or href.endswith('.mp4'):
                    file_url = href
                    file_name = os.path.basename(file_url)
                    file_path = os.path.join(download_folder, file_name)
                    with open(file_path, 'wb') as file:
                        file.write(requests.get(file_url).content)

                    print(f"Downloaded: {file_name}")

        print("Media files extraction completed.")
    else:
        print("Failed to retrieve content from the target URL.")

# Example Usage
download_folder = 'output/media_files'
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

extract_media_files(download_folder)