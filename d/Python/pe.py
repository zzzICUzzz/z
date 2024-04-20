import os
import shutil
from bs4 import BeautifulSoup

# Đường dẫn đến thư mục nguồn và đích
source_dir = r"C:\Users\mayde\Desktop\uptodate 2024\New folder (2)\testing\d\html"
dest_dir = r"C:\Users\mayde\Desktop\uptodate 2024\New folder (2)\testing\d\Patient education"

# Lấy danh sách tất cả các tệp HTML trong thư mục nguồn
html_files = [f for f in os.listdir(source_dir) if f.endswith(".html")]
total_files = len(html_files)

# Duyệt qua tất cả các tệp trong thư mục nguồn
for i, filename in enumerate(html_files):
    # Mở và phân tích tệp HTML
    with open(os.path.join(source_dir, filename), 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Kiểm tra xem tiêu đề có chứa "Patient education" không
    if soup.title and "Patient education" in soup.title.string:
        # Di chuyển tệp đến thư mục đích
        shutil.move(os.path.join(source_dir, filename), dest_dir)

    # In ra phần trăm đã quét
    print(f"Đã quét: {((i+1)/total_files)*100:.2f}%")
