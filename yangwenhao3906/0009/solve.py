# 一个HTML文件，找出里面的链接。

from bs4 import BeautifulSoup

def extract_html_hyperlinks(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        
        soup = BeautifulSoup(content, "html.parser")
        
        links = soup.find_all('a')
        
        for link in links:
            href = link.get('href')
            if href:
                print(href)
                
extract_html_hyperlinks("test.html")