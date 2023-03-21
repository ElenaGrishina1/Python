# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import os
os.system('cls') 
from random import randint

countN = int(input("Введите число монеток: "))
tailside = 0
other_side = 0
count = 0
for i in range(countN):
    x = randint(0, 1)
    if x == 0:
        other_side += 1
    else:
        tailside += 1
    print(x)
if other_side >= tailside:
    count = countN - other_side
else:
    count = countN - tailside
print('Минимальное количество монет, которые нужно перевернуть:', count)