# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

print()
print("Данная программа, преобразовывает десятичное число в двоичное.")
print()
user_data = int(input("Введите число, которое вы хотите преобразовать: "))

binary = []

number = user_data
half = user_data
count = 0

while count < 8:
    if number < 1:
        break
    else:
        half = int((number / 2))
        num = binary.append(int(number - (half * 2)))
        number = half
        count += 1

binary.reverse()

print()
print("Число", user_data, "в двоичном представлении: ",*binary)



