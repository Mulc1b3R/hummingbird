import os

def create_search_engines_page():
    search_engines = {
        'Google': 'https://www.google.com/',
        'Bing': 'https://www.bing.com/',
        'Yahoo': 'https://www.yahoo.com/',
        'DuckDuckGo': 'https://duckduckgo.com/'
        # Add more search engines and their URLs as needed
    }

    # Read the contents of the template file
    with open('template2.html', 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()

    # Generate the list of search engine links
    search_engines_list = '\n<ul>\n'
    for engine, url in search_engines.items():
        search_engines_list += f'<li><a href="{url}" target="_blank">{engine}</a></li>\n'
    search_engines_list += '</ul>\n'

    # Insert the search engine links into the template
    final_content = template_content.replace('<!-- SEARCH_ENGINES_LIST -->', search_engines_list)

    with open('output/engines.html', 'w', encoding='utf-8') as file:
        file.write(final_content)

    print("engines.html with the list of search engines has been created in the output folder.")
    return os.path.abspath('output/engines.html')

# Create engines.html with the list of search engine links
search_engines_page = create_search_engines_page()

# Open the engines.html file in the default web browser
os.system(f"start {search_engines_page}")