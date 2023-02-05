import random

print()
list_size = int(input("Введите размер списка: "))

user_list = []

counter = 0

while counter < list_size:
    i = user_list.append(random.randint(1, 11))
    counter += 1

print()
print("Сгенерированный список: ", user_list)
print()

positiveIndex = 0 
minusIndex = -1

len_user_list = len(user_list) 
iterations = len_user_list / 2

if iterations % 2 == 0:
    count = 0
    print("Ответ: ", end = " | ")
    while count < iterations:
        prod = print(user_list[positiveIndex] * user_list[minusIndex], end = " | ")
        minusIndex -= 1
        positiveIndex += 1
        count += 1
else:
    count = 0
    print("Ответ: ", end = " | ")
    while count < iterations:
        prod = print(user_list[positiveIndex] * user_list[minusIndex], end = " | ")
        minusIndex -= 1
        positiveIndex += 1
        count += 1

print()