import os
import shutil

def merge_files_from_folders(source_folder):
    # Lấy tất cả các thư mục con
    subfolders = [f.path for f in os.scandir(source_folder) if f.is_dir()]

    for subfolder in subfolders:
        files = os.listdir(subfolder)
        for file in files:
            shutil.move(os.path.join(subfolder, file), source_folder)
        os.rmdir(subfolder)

# Sử dụng hàm
merge_files_from_folders(r'C:\Users\mayde\Desktop\z\z\d\html')
