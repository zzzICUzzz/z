import json
import re

# Đường dẫn tới tệp JSON của bạn
file_path = r"C:\Users\mayde\Desktop\uptodate 2024\New folder (2)\testing\d\drug.json"

# Mở và đọc tệp
with open(file_path, 'r') as file:
    data = file.read()

# Sử dụng biểu thức chính quy để thay thế tất cả các dấu hai chấm ':' đi sau một chữ cái bằng một khoảng trắng
modified_data = re.sub(r'([a-zA-Z]):', r'\1', data)

# Ghi dữ liệu đã sửa đổi trở lại tệp
with open(file_path, 'w') as file:
    file.write(modified_data)
