Обработка изображений

```
import os
from PIL import Image, ImageDraw, ImageColor, ImageFont

#3.1. Напишите программу, которая получает на вход два типа (расширения) графических форматов,
# находит в текущем каталоге все графические файлы, соответствующие первому расширению,
# и конвертирует их в графический формат по второму расширению.


def img_chng(ext_1, ext_2):
    curr_path = os.getcwd()
    files = os.listdir(curr_path)
    for i in files:
        filename, file_extension = os.path.splitext(i)
        if file_extension == ext_1:
            im = Image.open(i)
            im.save(f'{filename}{ext_2}')
            os.remove(i)


#3.2. Дополните предыдущую функцию рисованием в центре изображения незаполненного квадрата,
# внутри которого будут написаны две строчки (вторая с новой строки):

#Hello,
#World!


def img_chng_draw(ext_1, ext_2):
    curr_path = os.getcwd()
    files = os.listdir(curr_path)
    for i in files:
        filename, file_extension = os.path.splitext(i)
        if file_extension == ext_1:
            im = Image.open(i)
            draw = ImageDraw.Draw(im)
            font = ImageFont.load_default()
            sz = im.size
            x_min = sz[0]/2 - 100
            y_max = sz[1]/2 - 100
            x_max = sz[0]/2 + 100
            y_min = sz[1]/2 + 100
            draw.rectangle([x_min, y_max, x_max, y_min])
            font = ImageFont.load_default().font_variant(size=20)
            text_x = sz[0]/2 - 20
            text_y = sz[1]/2 - 20
            draw.multiline_text((text_x, text_y), 'Hello,\nWorld!', font = font)
            im.save(f'{filename}{ext_2}')
            del draw
            os.remove(i)
            im.show()


img_chng('.jpeg', '.bmp')

img_chng_draw('.bmp', '.jpeg')
```

# Вывод функции:

![func](https://i.imgur.com/WjptXQo.png)