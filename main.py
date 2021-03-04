from PIL import Image, ImageDraw  # Подключим необходимые библиотеки.
import math
#функция выводит разницу между двумя цветами
def difcolor(a,b):

    k = math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2)+((a[2]-b[2])**2))

    return (k)


image = Image.open("fargo_8.jpg")  # Открываем изображение.
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
width = image.size[0]  # Определяем ширину.
height = image.size[1]  # Определяем высоту.
pix = image.load()  # Выгружаем значения пикселей.
#123
sp = 13
#123321
colors =[]
colors.append((159,180,191))
colors.append((100,123,119))
colors.append((39,72,92))
colors.append((146,159,156))
colors.append((192,34,23))
colors.append((191,204,210))
colors.append((224,206,192))
colors.append((233,234,234))
colors.append((223,145,90))
colors.append((105,148,170))



#для индикатора загрузки
for i in range(0,100):
    print("#",end="")
print()
pr = width*height
w1 = 0
w2 =1


for j in range(0,height-sp):
    for i in range(7,width-sp):


        #для индикатора загрущзки
        w1 = int((j * width + i) / (pr) * 100)
        if w2!=w1:
            print("#",end="")
        w2 = int((j*width + i)/(pr)*100)


        if i % sp == 0 and j % sp == 0:


            #расчет среднего цвета пикселей в клетке
            k=0
            c1 =0
            c2 =0
            c3 =0
            for a in range(0,sp):
                for b in range(0, sp):
                    k+=1
                    c1 += pix[i + a, j + b][0]
                    c2 += pix[i + a, j + b][1]
                    c3 += pix[i + a, j + b][2]
            c1 = int(c1/k)
            c2 = int(c2/k)
            c3 = int(c3/k)
            nclr = (c1,c2,c3)
            #print(nclr)
            fr = 500
            for cc in range(0,len(colors)):
                difclr = difcolor(nclr,colors[cc])


                if fr > difclr:
                    fr = difclr
                    nclr = colors[cc]




            #прорисовка
            for a in range(0,sp):
                for b in range(0, sp):
                    pix[i+a,j+b]= nclr
#print(len(colors))
image.show()