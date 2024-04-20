import os
from bs4 import BeautifulSoup

# Define the folder path and title to search for
folder_path = r'C:\Users\mayde\Desktop\uptodate 2024\New folder (2)\testing\d\del'
title_to_delete = "UpToDate-2024- بروزترین آپتودیت ایران- بیشترین رکورد ثبت کتب"

# Check if the folder exists
if os.path.isdir(folder_path):
    # Iterate over each file in the directory
    for filename in os.listdir(folder_path):
        if filename.endswith(".html"):
            file_path = os.path.join(folder_path, filename)
            
            # Open and read the file
            with open(file_path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')
                # Check if the title tag contains the specified title
                if soup.title and soup.title.string == title_to_delete:
                    os.remove(file_path)
                    print(f"Deleted file: {filename}")
