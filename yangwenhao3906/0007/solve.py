# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import os
# import 

def count_code(folder_name):

    line_of_code = 0
    line_of_comment = 0
    line_of_blank = 0

    for file_name in os.listdir(folder_name):

        file_path = os.path.join(folder_name, file_name)

        with open(file_path) as file:

            lines = file.readlines()

            for line in lines:
                # 去除前后空格
                line = line.strip()
                
                if not line: # 空行
                    line_of_blank += 1
                elif line.startswith('#'): # 注释
                    line_of_comment += 1
                else:
                    line_of_code += 1

            # line_of_code += (len(lines) - line_of_blank - line_of_comment)
    
    print("line_of_code: ", line_of_code)
    print("line_of_comment: ", line_of_comment)
    print("line_of_blank: ", line_of_blank)

count_code("code_field")