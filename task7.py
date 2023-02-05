

import random

print()
print("Данная программа самый близкий по величине элемент к числу, которое задаст пользователь.")

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
