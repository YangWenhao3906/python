# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。1136x640

import os
from PIL import Image

def adapt_pic_size_to_iPhone5(folder_path):

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".jpg") or file_name.endswith(".png") or file_name.endswith(".jpeg"):
            file_path = os.path.join(folder_path, file_name)

            image = Image.open(file_path)

            original_size = image.size
            width, height = original_size

            if width <= 1136 and height <= 640:
                new_size = original_size
            elif width > 1136 and height <= 640:
                new_size = (1136, int(height*1136/width))
            elif width <= 1136 and height > 640:
                new_size = (int(width*640/height), 640)
            else:
                if width/1136 > height/640:
                    new_size = (1136, int(height*1136/width))
                else:
                    new_size = (int(width*640/height), 640)
            
            resize_image = image.resize(new_size)

            with open(file_name,"w"):
                resize_image.save(file_name)

adapt_pic_size_to_iPhone5("photo")