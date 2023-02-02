# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai Последняя строка
# содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

import random

print()
arr_size = int(input("Введите размер массива: "))
print()

user_arr = []

count = 0

while count < arr_size:
    i = user_arr.append(random.randint(1, 20))  
    count += 1

print()
print(user_arr)
print()

user_number = int(input("Введите число: "))

near = 0
for i in user_arr:
    if i > near and i <= user_number:
        near = i
    else:
        continue

print()
print("Максимально приближенное число: ", near)
