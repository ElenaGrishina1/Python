# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

import os
os.system('cls') 
nam = int(input('Введите трехзначное число: '))
summ = (nam % 10) + (nam % 100 // 10) + (nam // 100)
print(f'Сумма цифр трехзначного числа {summ}')
