
print()
print("Данная программа вычисляет стоимость введенного пользователем слова")
print()

user_word_input = str(input("Введите, пожалуйста, слово: ")) 

points = 0

eng = 0
ru = 0

lang_check = str("Ошибка ввода. Слово должно содержать либо только английские, либо только русские буквы.")
flag = str("Ошибка ввода. Введите, пожалуйста, одно слово целиком.")

# Английские символы
for i in user_word_input: 
    if i == 'A' or i == 'E' or i == 'I' or i =='O' or i == 'U' or i == 'L' or i == 'N' or i == 'S' or i == 'T' or i == 'R':
        points += 1
        eng += 1
    if i == 'a' or i == 'e' or i == 'i' or i =='o' or i == 'u' or i == 'l' or i == 'n' or i == 's' or i == 't' or i == 'r':
        points += 1
        eng += 1
    if i == 'D' or i == 'G':
        points += 2
        eng += 1
    if i == 'd' or i == 'g':
        points += 2
        eng += 1
    if i == 'B' or i == 'C' or i == 'M' or i == 'P':
        points += 3
        eng += 1
    if i == 'b' or i == 'c' or i == 'm' or i == 'p':
        points += 3
        eng += 1
    if i == 'F' or i == 'H'or i == 'V' or i == 'W' or i == 'Y':
        points += 4
        eng += 1
    if i == 'f' or i == 'h'or i == 'v' or i == 'w' or i == 'y':
        points += 4
        eng += 1
    if i == 'K':
        points += 5
        eng += 1
    if i == 'k':
        points += 5
        eng += 1
    if i == 'J' or i == 'X':
        points += 8
        eng += 1
    if i == 'j' or i == 'x':
        points += 8
        eng += 1
    if i == 'Q' or i == 'Z':
        points += 10
        eng += 1
    if i == 'q' or i == 'z':
        points += 10
        eng += 1
    if i == ' ' or i == '-' or i == '-' or i == ',' or i == '.':
        points = 0
        break

# Русские символы
for i in user_word_input: 
    if i == 'А' or i == 'В' or i == 'Е' or i =='И' or i == 'Н' or i == 'О' or i == 'Р' or i == 'С' or i == 'Т':
        points += 1
        ru += 1
    if i == 'а' or i == 'в' or i == 'е' or i =='и' or i == 'н' or i == 'о' or i == 'р' or i == 'с' or i == 'т':
        points += 1
        ru += 1
    if i == 'Д' or i == 'К' or i == 'Л' or i == 'М' or i == 'П' or i == 'У':
        points += 2
        ru += 1
    if i == 'д' or i == 'к' or i == 'л' or i == 'м' or i == 'п' or i == 'у':
        points += 2
        ru += 1   
    if i == 'Б' or i == 'Г' or i == 'Ё' or i == 'Ь' or i == 'Я':
        points += 3
        ru += 1
    if i == 'б' or i == 'г' or i == 'ё' or i == 'ь' or i == 'я':
        points += 3
        ru += 1
    if i == 'Й' or i == 'Ы':
        points += 4
        ru += 1
    if i == 'й' or i == 'ы':
        points += 4
        ru += 1
    if i == 'Ж' or i == 'З' or i == 'Х' or i == 'Ц' or i == 'Ч':
        points += 5
        ru += 1
    if i == 'ж' or i == 'з' or i == 'х' or i == 'ц' or i == 'ч':
        points += 5
        ru += 1
    if i == 'Ш' or i == 'Э' or i == 'Ю':
        points += 8
        ru += 1
    if i == 'ш' or i == 'э' or i == 'ю':
        points += 8
        ru += 1
    if i == 'Ф' or i == 'Щ' or i == 'Ъ':
        points += 10
        ru += 1
    if i == 'ф' or i == 'щ' or i == 'ъ':
        points += 10
        ru += 1
    if i == ' ' or i == '-' or i == '-' or i == ',' or i == '.':
        points = 0
        break

if eng > 0 and ru > 0:
    print(lang_check)
elif points == 0:
    print()
    print(flag)
else:
    print()
    print("Ваше слово приносит Вам", points, "очков.")