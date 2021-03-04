from PIL import Image, ImageDraw  # Подключим необходимые библиотеки.

image = Image.open("fargo_8.jpg")  # Открываем изображение.
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
width = image.size[0]  # Определяем ширину.
height = image.size[1]  # Определяем высоту.
pix = image.load()  # Выгружаем значения пикселей.

pr = width*height
colors = []
for w in range(0, width):
    for h in range(0,height):
        if not (pix[w,h] in colors):
            colors.append(pix[w,h])
            print(int((w * width + h) / (pr) * 100))

print(len(colors))

