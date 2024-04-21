from bs4 import BeautifulSoup
import os
import glob
from tqdm import tqdm

def replace_in_files(dir_path, old1, new1, old2):
    # Get list of all .html files in the specified directory
    files = glob.glob(os.path.join(dir_path, "*.html"))

    # Initialize progress bar
    pbar = tqdm(total=len(files), desc="Processing files", ncols=100)

    for file in files:
        # Read the file
        with open(file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        # Convert the soup to string so we can use replace
        html = str(soup)

        # Replace the target string
        html = html.replace(old1, new1)
        html = html.replace(old2, '')

        # Write the file out again
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)

        # Update progress bar
        pbar.update(1)

    # Close progress bar
    pbar.close()

# Specify the directory path
dir_path = r"C:\Users\mayde\Desktop\z\d\html\folder_6"

# Call the function
replace_in_files(dir_path, '/d/', '/z/d/', 'medilib.ir')
