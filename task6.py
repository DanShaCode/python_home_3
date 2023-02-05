
import random

print()
print("Данная программа отвечает на вопрос пользователя.")
print() 
print("Cколько раз повторяется то, или иное число из случайно заданного списка?")
print()
print("Размер списка задает пользователь.")

print()
user_size = int(input("Введите размер массива: ")) 
print()

user_list = []

count = 0

while count < user_size: 
    i = user_list.append(random.randint(1, 10))
    count += 1

print("Сгенерированный список: ", user_list) 

max = 0

for i in user_list: 
    if i > max:
        max = i

counter = []
counter_len = max + 1
count = 0

while count < counter_len: 
    i = counter.append(0)
    count += 1

count = 0
j = int(0)

while count < len(user_list): 
    if i != 0:
        counter[user_list[j]] += 1
        j += 1
        count += 1
    else:
        j += 1
        count += 1

print()
x = int(input("Введите число из списка: "))

flag = 0
for i in user_list:
    if x == i:
        flag += 1
        print()
        print("Данное число встречается в списке", counter[x], "раз(а).")
        break
    else:
        continue

if flag == 0:
    print()
    print("Такого числа в списке нет.")