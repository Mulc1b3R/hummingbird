import os
from urllib.parse import urlparse
import shutil
import zipfile

def get_target_url_from_env():
    with open('.env', 'r') as file:
        for line in file:
            if line.startswith('TARGET_URL='):
                return line.strip().split('=')[1]

def move_and_rename_output_folder(target_url):
    output_folder = os.path.join(os.getcwd(), 'output')
    target_domain = urlparse(target_url).netloc

    if not os.path.exists(output_folder):
        print("The 'output' folder does not exist.")
        return

    archive_folder = os.path.join(os.getcwd(), 'archive')
    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)

    new_folder_name = os.path.join(archive_folder, target_domain)
    os.makedirs(new_folder_name)

    # Move contents of 'output' folder to the new folder
    for item in os.listdir(output_folder):
        s = os.path.join(output_folder, item)
        d = os.path.join(new_folder_name, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks=False)
        else:
            shutil.copy2(s, d)

    # Zip the new folder
    zip_filename = os.path.join(archive_folder, f'{target_domain}.zip')
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(new_folder_name):
            for file in files:
                file_path = os.path.relpath(os.path.join(root, file), new_folder_name)
                zipf.write(os.path.join(root, file), file_path)

    print(f"'output' folder contents moved and archived as '{target_domain}.zip' successfully.")

    # Clean up: delete contents of the 'output' folder
    for item in os.listdir(output_folder):
        item_path = os.path.join(output_folder, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

    print("Contents of 'output' folder have been deleted.")

# Extract the target URL from the .env file
target_url = get_target_url_from_env()

if target_url is not None:
    move_and_rename_output_folder(target_url)
else:
    print("Target URL not found in the .env file.")