# 一个HTML文件，找出里面的正文。

# <!DOCTYPE html>
# <html>
# <head>
#     <title>我的网页</title>
# </head>
# <body>
#     <!-- 正文内容 -->
# </body>
# </html>

import re

def extract_html_body(file_name):
    with open(file_name) as f:
        content = f.read()
        pattern = r"<body>([\s\S]*?)<\/body>"
        
        match = re.search(pattern, content)
        
        if match:
            print("match found")
            body_content = match.group(1)
            print(body_content)
        else:
            print("match not found")

extract_html_body("test.html")