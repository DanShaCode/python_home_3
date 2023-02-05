import random

print()
print("Данная программа самый близкий по величине элемент к числу, который задаст пользователь.")

print()
arr_size = int(input("Введите размер списка: "))

user_arr = []

count = 0

while count < arr_size:
    i = user_arr.append(random.randint(1, 100))  
    count += 1

print()
print(user_arr)
print()

user_number = int(input("Введите число: "))

for i in user_arr:
    if i == user_number:
        print()
        print("Максимально приближенное число: ", user_number)
        break
    elif user_number > max(user_arr) or user_number < min(user_arr):
        print()
        print("Такого числа в списке нет.")
        break
else:
    min_arr = []

    for i in user_arr:
        if i < user_number:
            min_arr.append(i)

    minimum = max(min_arr)

    max_arr = []

    for i in user_arr:
        if i > user_number:
            max_arr.append(i)
    
    maximum = min(max_arr)

    dif_max = maximum - user_number
    dif_min = user_number - minimum

    if dif_max < dif_min:
        print()
        print("Максимально приближенное число: ", maximum)
    elif dif_max > dif_min:
        print()
        print("Максимально приближенное число: ", minimum)
    elif dif_max == dif_min:
        print()
        print("Максимально приближенное число: ", minimum)