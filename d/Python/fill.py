import os
import shutil
from bs4 import BeautifulSoup

# Đường dẫn đến thư mục chứa các tệp HTML
source_folder = r"C:\Users\mayde\Desktop\uptodate 2024\New folder (2)\testing\d\html"

# Đường dẫn đến thư mục đích
dest_folder_graphic = r"C:\Users\mayde\Desktop\uptodate 2024\New folder (2)\testing\d\Society guideline links"
dest_folder_drug_info = r"C:\Users\mayde\Desktop\uptodate 2024\New folder (2)\testing\d\drug information"

# Lấy danh sách tất cả các tệp trong thư mục nguồn
files = [f for f in os.listdir(source_folder) if f.endswith(".html")]
total_files = len(files)

# Quét tất cả các tệp trong thư mục nguồn
for i, filename in enumerate(files, start=1):
    filepath = os.path.join(source_folder, filename)
    dest_path_graphic = os.path.join(dest_folder_graphic, filename)
    dest_path_drug_info = os.path.join(dest_folder_drug_info, filename)

    # Mở và phân tích tệp HTML
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

        # Kiểm tra nếu có thẻ div với id="graphicVersion"
        if "Society guideline links" in soup.title.string and not os.path.exists(dest_path_drug_info):
            try:
                shutil.move(filepath, dest_folder_graphic)
            except PermissionError:
                print(f"Permission denied for file {filepath}. Skipping this file.")
        # Kiểm tra nếu tiêu đề có chứa cụm từ "drug information"
        elif "Drug information" in soup.title.string and not os.path.exists(dest_path_drug_info):
            try:
                shutil.move(filepath, dest_folder_drug_info)
            except PermissionError:
                print(f"Permission denied for file {filepath}. Skipping this file.")

    # In ra phần trăm tiến trình thực thi
    print(f"Đã thực thi {i/total_files*100:.2f}%")
