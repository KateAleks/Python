import math
from msilib import PID_TITLE

x1 = int(input ('Введите координату x первой точки = '))
y1 = int(input ('Введите координату y первой точки = '))
x2 = int(input ('Введите координату x второй точки = '))
y2 = int(input ('Введите координату y второй точки = '))

dist = math.sqrt((x1-x2)**2+(y1-y2)**2)
print ('расстояние между точками =', dist) 