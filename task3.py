# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

print()
list_size = int(input("Введите размер списка: "))

user_list = []

count = 0

while count < list_size:
    i = user_list.append(float(round(random.uniform(1.0, 5.0), 1)))
    count += 1

fraction = []

for i in user_list:
    i = fraction.append(float(round(i % 1, 1)))

min = 1
for i in fraction:
    if i < min:
        min = i

max = 0
for i in fraction:
    if i > max:
        max = i

print()
print("Сгенерированный список: ", user_list)
print()
print("Ответ:", round(max - min, 2))