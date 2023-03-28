# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


import os
os.system('cls') 
n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))
spisok_1 = set(map(int, input(f'Введите {n} цифр через пробел: ').split()))
spisok_2 = set(map(int, input(f'Введите {m} цифр через пробел: ').split()))
n = len(spisok_1)
m = len(spisok_2)
spisok_3 = spisok_1.intersection(spisok_2)

print(f'Список уникальных цифр: {sorted(spisok_3)}')