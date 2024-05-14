import os
import webbrowser
from bs4 import BeautifulSoup
import requests

def open_in_popup(file_path):
    webbrowser.open('file://' + file_path, new=1)  

def create_index_html(output_folder, url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        with open(f"{output_folder}/index.html", "w", encoding="utf-8") as file:
            file.write(soup.prettify())

def create_iframe_html(output_folder, target_url):
    iframe_content = f"""
    <html>
    <head>
        <link rel="icon" type="image "a href="../hummingbird.gif">
        <style>
          /* CSS styles omitted for brevity */
        </style>
    </head>
    <body>
        <center>
            <h1>HummingBird: Target url identified...</h1>
        </center>
        <iframe src='{target_url}' width='100%' height='800px'></iframe>
        <!-- Other content omitted for brevity -->
    </body>
    </html>
    """
    with open(f"{output_folder}/iframe.html", "w", encoding="utf-8") as file:
        file.write(iframe_content)

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

    return env_vars

def scrape_url(target_url):
    output_folder = 'output'
    os.makedirs(output_folder, exist_ok=True)

    create_index_html(output_folder, target_url)
    create_iframe_html(output_folder, target_url)

    file_path = os.path.abspath(f"{output_folder}/iframe.html")
    open_in_popup(file_path)

    print("Index and iframe HTML files created successfully in the 'output' folder.")

if __name__ == "__main__":
    env_vars = load_env()
    target_url = env_vars.get('TARGET_URL')

    if not target_url:
        print("Target URL not found in the .env file.")
    else:
        scrape_url(target_url)