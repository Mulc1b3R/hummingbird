import os
import shutil

def clean_archive_folder():
    archive_folder = os.path.join(os.getcwd(), 'archive')

    if not os.path.exists(archive_folder):
        print("The 'archive' folder does not exist.")
        return

    for item in os.listdir(archive_folder):
        item_path = os.path.join(archive_folder, item)
        if os.path.isdir(item_path) and not item.endswith('.zip'):
            shutil.rmtree(item_path)
            print(f"Deleted '{item}' folder.")

    print("Archive folder contents eradicated.")

clean_archive_folder()