import math
#функция выводит разницу между двумя цветами
def difcolor(a,b):

    k = math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2)+((a[2]-b[2])**2))

    return (k)


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

for i in range(0,len(colors)):
    print(difcolor((192,34,23),colors[i]))