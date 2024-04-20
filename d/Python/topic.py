import os
from bs4 import BeautifulSoup

# Đường dẫn đến thư mục chứa các tệp HTML
folder_path = r"C:\Users\mayde\Desktop\uptodate 2024\New folder (2)\testing\d\html"

# Lấy danh sách tất cả các tệp HTML trong thư mục
all_files = [f for f in os.listdir(folder_path) if f.endswith(".html")]
total_files = len(all_files)

# Duyệt qua tất cả các tệp trong thư mục
for i, filename in enumerate(all_files):
    file_path = os.path.join(folder_path, filename)

    # Mở và đọc tệp
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()

    # Phân tích cú pháp HTML
    soup = BeautifulSoup(contents, 'lxml')

    # Kiểm tra xem tệp có chứa div với id="graphicVersion" hoặc tiêu đề chứa các cụm từ chỉ định không
    if soup.find(id="graphicVersion") or any(keyword in soup.title.string for keyword in ["Society guideline links","Patient education","Drug information","drug information", "UpToDate-2024- بروزترین آپتودیت ایران- بیشترین رکورد ثبت کتب"]):
        # Nếu có, xóa tệp
        os.remove(file_path)
        print(f"Đã xóa tệp: {file_path}")

    # In ra phần trăm số tệp đã được quét
    print(f"Đã quét {((i+1)/total_files)*100:.2f}%")
