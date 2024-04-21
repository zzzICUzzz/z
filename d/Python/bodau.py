import json
import re

# Đường dẫn tới tệp JSON của bạn
file_path = r"C:\Users\mayde\Desktop\z\d\drug.json"

# Mở và đọc tệp
with open(file_path, 'r') as file:
    data = file.read()

# Sử dụng biểu thức chính quy để thay thế tất cả các dấu hai chấm ':' đi sau một chữ cái bằng một khoảng trắng
modified_data = re.sub(r'([a-zA-Z]):', r'\1', data)

# Thêm tính năng để xóa tất cả dấu phẩy mà sau là một chữ cái
modified_data = re.sub(r'([a-zA-Z]),', r'\1', modified_data)

# Chuyển tất cả chữ hoa thành chữ thường
modified_data = modified_data.lower()

# Ghi dữ liệu đã sửa đổi trở lại tệp
with open(file_path, 'w') as file:
    file.write(modified_data)
