import json

# Đường dẫn đến file JSON
file_path = r"C:\Users\mayde\Desktop\z\z\d\trans.json"

# Mở và đọc file JSON
with open(file_path, 'r') as f:
    data = json.load(f)

# Lọc ra các title có chữ "calculator" và loại bỏ đuôi .html
filtered_files = [file.split('.html')[0] for file, title in data.items() if 'calculator' in title.lower()]

# Xuất ra danh sách tên file
for file in filtered_files:
    print(file + ',')
