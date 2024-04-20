import os
import re
import time

# Đường dẫn đến thư mục chứa các tệp HTML
html_folder_path = "C:\\Users\\mayde\\Desktop\\uptodate 2024\\New folder (2)\\testing\\d\\html\\folder_11"

# Đường dẫn đến các tệp txt
txt_file_paths = {
    "graphic": "C:\\Users\\mayde\\Desktop\\uptodate 2024\\New folder (2)\\testing\\d\\graphic.txt",
    "drug information": "C:\\Users\\mayde\\Desktop\\uptodate 2024\\New folder (2)\\testing\\d\\drug infomation.txt"
}

# Đọc các tệp txt và lưu tất cả các tên tệp vào một set
file_names = {}
for key, txt_file_path in txt_file_paths.items():
    with open(txt_file_path, "r") as txt_file:
        file_names[key] = set(name.strip("'") for name in txt_file.read().split(','))

# Duyệt qua tất cả các tệp HTML trong thư mục
html_files = os.listdir(html_folder_path)
total_files = len([name for name in html_files if name.endswith(".html")])

for i, filename in enumerate(html_files):
    if filename.endswith(".html"):
        file_path = os.path.join(html_folder_path, filename)

        # Đọc nội dung tệp
        with open(file_path, "r", encoding='utf-8') as html_file:
            content = html_file.read()

        # Tìm tất cả các chuỗi khớp với "/html/*.html"
        for match in re.findall(r"/html/(\d+).html", content):
            # Nếu tên tệp tồn tại trong tệp txt, thay thế chuỗi
            for key in file_names:
                if match + ".html" in file_names[key]:
                    content = content.replace(f"/html/{match}.html", f"/{key}/{match}.html")

        # Ghi lại nội dung đã được thay đổi vào tệp
        with open(file_path, "w", encoding='utf-8') as html_file:
            html_file.write(content)

        # In ra tiến trình công việc
        print(f"Đã xử lý xong {i+1}/{total_files} tệp.")

print("Hoàn thành công việc!")
