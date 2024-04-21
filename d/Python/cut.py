import os
import shutil

def divide_files_into_folders(source_folder, num_files_per_folder):
    files = os.listdir(source_folder)
    for i in range(0, len(files), num_files_per_folder):
        folder_name = os.path.join(source_folder, f'folder_{i // num_files_per_folder + 1}')
        os.makedirs(folder_name, exist_ok=True)
        for file in files[i:i + num_files_per_folder]:
            shutil.move(os.path.join(source_folder, file), folder_name)

# Sử dụng hàm
divide_files_into_folders(r'C:\Users\mayde\Desktop\z\d\html', 2000)
