from PIL import Image, ImageFilter, ImageDraw, ImageFont
import requests

# img = Image.open('picture.png')  # Выбор изображения
# img.show()  # Отображение изображения

# print(img.size)  # Размер изображения
# print(img.format)  # Формат изображения
# print(img.mode)  # Режим изображения
# print(img.histogram)  # Гистограмма изображения

# img.thumbnail((200, 200))  # Изображение 200x200
# img.save('mini_img.png')  # Сохранение изображения
# img.show()

# crop_img = img.crop((100, 200, 300, 400))  # Обрезка изображения
# crop_img.save('cropped.png')
# crop_img.show()

# rotate_img = img.rotate(120)  # Поворот изображения
# rotate_img.save('rotate_img.png')
# rotate_img.show()

"""Фильтры изображений: BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS,
FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN"""

# blurred_img = img.filter(ImageFilter.BLUR)  # Фильтр изображения
# blurred_img.save('blurred_img.png')
# blurred_img.show()

# img = Image.new('RGBA', (400, 200), 'gray')  # Создаем серый холст
# img_draw = ImageDraw.Draw(img)
# img_draw.rectangle((20, 20, 100, 100), fill='red')  # Рисуем красный прямоугольник
# headline = ImageFont.truetype('arial.ttf', size=30)
# text = 'Hello World!'
# img_draw.text((120, 60), text, font=headline)  # Пишем текст
# img.save('img_draw.png')
# img.show()

url = input('Address:::> ')  # Загрузка изображения с интернета
response = requests.get(url, stream=True).raw
img = Image.open(response)
img.save('img.png')
img.show()
