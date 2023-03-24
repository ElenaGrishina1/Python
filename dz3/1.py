# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

import os
os.system('cls')
import random

n = int(input("Введите количество элементов в массиве: "))
my_list = [random.randint(0, 10) for i in range(n)]
print(my_list)

x = int(input("Введите число X, которое необходимо найти в массиве: "))
count = 0
for i in range(n):
    if my_list[i] == x:
        count += 1
print(f"Число {x} в массиве встречается: {count} раз/а)")
