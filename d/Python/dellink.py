import os
from bs4 import BeautifulSoup

folder_path = r"C:\Users\mayde\Desktop\z\z\d\html\folder_6"

html_files = [f for f in os.listdir(folder_path) if f.endswith(".html")]
total_files = len(html_files)

for i, filename in enumerate(html_files, start=1):
    filepath = os.path.join(folder_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    head = soup.head
    title = head.title

    # Xóa tất cả nội dung ở phần head
    for tag in head.find_all(True):
        tag.extract()

    # Giữ lại phần title
    head.append(title)

    # Thêm vào head nội dung <link href="d/css/1.css" rel="stylesheet"/>
    new_tag = soup.new_tag("link", href="d/css/1.css", rel="stylesheet")
    head.append(new_tag)

    html = soup.prettify("utf-8")
    with open(filepath, "wb") as file:
        file.write(html)

    print(f"Đã xử lý xong tệp {i} trên {total_files}.")
