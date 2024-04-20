import os,re
from bs4 import BeautifulSoup

folder_path = r'C:\Users\mayde\Desktop\uptodate 2024\New folder (2)\testing\d\html'
classes_to_remove = ['main-header-area header-sticky','uptodate-area sticky','newsletter-area', 'buyPackage','modal fade text-left','goback',
                     'footer-area','modal fade','pwaprompt']
def sua_file_html(file_path, classes_to_remove):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
        
        # Giữ lại thẻ <title> và <link rel="stylesheet">
        if soup.head:
            title_tag = soup.head.title
            link_tags = soup.head.find_all('link', rel='stylesheet')
            soup.head.clear()
            if title_tag:
                soup.head.append(title_tag)
            for link_tag in link_tags:
                soup.head.append(link_tag)
        
        # Xóa tất cả thẻ <script>
        for script in soup(["script"]):
            script.extract()
        
        # Xóa các class được chỉ định
        for class_name in classes_to_remove:
            for tag in soup.find_all(class_=class_name):
                tag.decompose()
        
        # Xóa thẻ div có id là "search-area"
        div_to_remove = soup.find('div', id='search-area')
        if div_to_remove:
            div_to_remove.extract()
        
        # Thay thế toàn bộ chuỗi "https://medilib.ir/assets" bằng chuỗi "/d"
        html_as_str = str(soup)
        html_as_str = html_as_str.replace("https://medilib.ir/assets", "/d")
        # Thay thế toàn bộ chuỗi "https://medilib.ir/assets" bằng chuỗi "/d"
        html_as_str = str(soup)
        html_as_str = html_as_str.replace("https://medilib.ir/assets", "/d")
        
        # Thay thế URL theo yêu cầu
        html_as_str = re.sub(r"https://medilib\.ir/uptodate/show/(\d+)", r"/d/html/\1.html", html_as_str)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_as_str)

for filename in os.listdir(folder_path):
    if filename.endswith(".html"): # chỉ xử lý các tệp HTML
        file_path = os.path.join(folder_path, filename)
        print(f"Đang xử lý: {file_path}" )
        sua_file_html(file_path, classes_to_remove)
