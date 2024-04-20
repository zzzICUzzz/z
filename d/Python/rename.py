import os
from bs4 import BeautifulSoup

folder_path = r'C:\Users\mayde\Desktop\uptodate 2024\New folder (2)\testing\đã lọc'
for filename in os.listdir(folder_path):
    print (filename)
    if filename.endswith('.txt'):
        # Tạo đường dẫn tệp nguồn và đích
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, filename.replace('.txt', '.html'))
        # Đổi tên tệp
        os.rename(src, dst)
