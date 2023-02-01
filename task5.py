# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

fibo = [0,1]

count = 0
a = int(0)
b = int(1)

while count < 7:
    temp = b
    b = a + b
    app = fibo.append(b)
    a = temp
    count += 1

index = 1
counter = 1
j = 0

while counter < 9:
    if counter % 2 != 0:
        print(fibo[index])
        fibo.insert(j, fibo[index])
        index += 2
        counter += 1
    else:
        print(fibo[index])
        minus = fibo[index] * (-1)
        fibo.insert(j, minus)
        index += 2
        counter += 1

print()
print(fibo)