import os
import random
import string
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def generate_random_external_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    external_links = []
    for link in soup.find_all('a', href=True):
        href = link.get('href')
        if href and 'http' in href and urlparse(url).netloc not in href:
            external_links.append(href)

    return external_links

def create_patchwork_html(output_dir, images, external_links):
    with open(os.path.join(output_dir, 'patchwork.html'), 'w') as html_file:
        html_file.write('<html>\n<head>\n<title>Patchwork</title>\n</head>\n<body>\n')
        html_file.write('<div style="display: flex; flex-wrap: wrap; justify-content: center;">\n')

        for idx, img in enumerate(images):
            if idx < len(external_links):
                random_link = random.choice(external_links)
                html_file.write(f'<a href="{random_link}"><img src="img/{img}" style="margin: 5px; max-width: 200px; max-height: 200px;"></a>\n')
            else:
                html_file.write(f'<img src="img/{img}" style="margin: 5px; max-width: 200px; max-height: 200px;">\n')

        html_file.write('</div>\n</body>\n</html>')

def embed_patchwork_in_template(output_dir):
    with open(os.path.join(output_dir, 'patchwork.html'), 'r') as f:
        content = f.read()

    with open('template3.html', 'r') as template_file:
        template_content = template_file.read()
        final_content = template_content % content

    with open(os.path.join(output_dir, 'output_patchwork.html'), 'w') as output_file:
        output_file.write(final_content)

output_folder = 'output'
website_url = 'https://zerohedge.com'  # Replace with the website URL you want to extract links from
img_dir = os.path.join(output_folder, 'img')
images = [f for f in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir, f))]
external_links = generate_random_external_links(website_url)
create_patchwork_html(output_folder, images, external_links)
embed_patchwork_in_template(output_folder)