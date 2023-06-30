from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def icon_message_unread_num(icon_file_path, message_unread_num) -> None:
    image = Image.open(icon_file_path)
    image_size = image.size
    font_size = int(image.size[1] / 4)
    print("image load success")

    font = ImageFont.truetype(font = 'arial.ttf', size = font_size)
    
    draw = ImageDraw.Draw(image)
    draw.text(xy = (image.size[0]-font_size, 0), text = str(message_unread_num), font = font)

    image.save("new.jpg")

icon_message_unread_num("hello.jpg",3)