
import requests

def load_env():
    env_vars = {}
    with open('.env', 'r') as file:
        for line in file:
            key, value = line.strip().split('=', 1)
            env_vars[key] = value
    return env_vars

# Load target URL from environment variables
env_vars = load_env()
target_url = env_vars.get('TARGET_URL')

if not target_url:
    print("Target URL not found in the .env file. Please set the TARGET_URL in the .env file.")
    exit()

def fetch_from_wikipedia(target_url):
    wikipedia_api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'extracts',
        'exintro': True,
        'titles': target_url,
    }
    response = requests.get(wikipedia_api_url, params=params)
    data = response.json()
    pages = data.get('query', {}).get('pages', {})
    if pages:
        page_id = next(iter(pages.keys()))
        summary = pages[page_id].get('extract', 'Summary not found on Wikipedia')
        return summary
    return 'Summary not found on Wikipedia'

def fetch_from_reddit(target_url):
    reddit_api_url = "https://www.reddit.com/search.json"
    params = {'q': target_url, 'limit': 5}
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(reddit_api_url, params=params, headers=headers)
    
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            post_titles = [post['data']['title'] for post in posts] if posts else ['No posts found on Reddit']
            return post_titles
        except Exception as e:
            print(f"Error processing Reddit data: {e}")
    else:
        print(f"Failed to retrieve data from Reddit. Status code: {response.status_code}")
    
    return ['No posts found on Reddit']

def fetch_from_additional_source(target_url):
    # Add code to fetch data from an additional source using the target URL
    # Customize this function to retrieve data from your chosen additional source
    return "Data from additional source"

# Fetch information from Wikipedia, Reddit, and additional source using the target URL
wikipedia_summary = fetch_from_wikipedia(target_url)
reddit_posts = fetch_from_reddit(target_url)
additional_data = fetch_from_additional_source(target_url)

# Save information to a text file
output_file = "output/organization_info.txt"
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(f"Wikipedia Summary:\n{wikipedia_summary}\n\nReddit Posts:\n")
    for idx, post_title in enumerate(reddit_posts, start=1):
        file.write(f"{idx}. {post_title}\n")
    file.write(f"\nAdditional Data:\n{additional_data}")
    print(f"Information fetched from Wikipedia, Reddit, and an additional source using the target URL. Output saved to {output_file}")