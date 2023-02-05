
import random

print()
print("Данная программа находит сумму элементов списка, стоящих на нечётной позиции.")

print()
n = int(input("Задайте, пожалуйста, размер списка: "))
print()

arr = []
count = 0

while count < n:
    i = arr.append(random.randint(0,10))
    count += 1

print()
print("Созданный список: ", arr)

sum = 0
index = 0

for i in arr:
    if index % 2 == 0:
        index += 1
    else:
        sum += i
        index += 1

print()
print("Сумма элементов списка на нечетных позициях списка: ", sum)