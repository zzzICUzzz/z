import os
import json
from bs4 import BeautifulSoup

def get_file_titles(folder_path):
    title_dict = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".html"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file.read(), 'html.parser')
                title = soup.title.string if soup.title else "No title"
                title_dict[filename] = title
                print (title_dict[filename])
    return title_dict

def write_titles_to_file(title_dict, output_file_path):
    # Đọc dữ liệu hiện có từ tệp
    try:
        with open(output_file_path, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    # Kết hợp dữ liệu hiện có với dữ liệu mới
    combined_data = {**existing_data, **title_dict}

    # Ghi dữ liệu kết hợp vào tệp
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(combined_data, file, ensure_ascii=False)

folder_path = r'C:\Users\mayde\Desktop\uptodate 2024\New folder (2)\testing\d\drug information\folder_4'
output_file_path = r'C:\Users\mayde\Desktop\uptodate 2024\New folder (2)\testing\d\drug.json'

title_dict = get_file_titles(folder_path)
write_titles_to_file(title_dict, output_file_path)
