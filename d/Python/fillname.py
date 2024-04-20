import os

# Đường dẫn đến thư mục bạn muốn quét
folder_path = r'C:\Users\mayde\Desktop\uptodate 2024\New folder (2)\testing\d\Society guideline links'

# Lấy tất cả tên file trong thư mục
file_names = os.listdir(folder_path)

# Lọc ra những file có đuôi là .html
html_files = [file for file in file_names if file.endswith('.html')]

# Đường dẫn đến file output
output_file_path = 'html_files.txt'

# Mở file output ở chế độ ghi
with open(output_file_path, 'w') as f:
    # Ghi danh sách tên các file HTML vào file output
    for html_file in html_files:
        f.write(f'{html_file}\\n')

print(f"Danh sách tên các file HTML đã được lưu thành công vào {output_file_path}.")
