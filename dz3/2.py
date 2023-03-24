# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import os
os.system('cls') 
import random

n = int(input("Введите количество элементов в массиве: "))
my_list = [random.randint(0, 10) for i in range(n)]
print(my_list)

x = int(input("Введите число X: "))
min = abs(x - my_list[0])
index = 0
for i in range(1, n):
    count = abs(x - my_list[i])
    if count < min:
        min = count
        index = i
print(f"Самый близкий по величине элемент к заданному числу {x} ->", my_list[index])