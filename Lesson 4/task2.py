# Пишем функцию, которая попросит ввести число. Пока он не введёт правильно, просите
# его ввести. Функция возвращает введённое число.
# * Теперь далее для других задач с числами, вы можете пользоваться этой функцией, а не
# простым input!


def enter_number():
    while True:
        number = input("Enter a number: ")
        try:
            number = float(number)
            print(number)
            return number
            break
        except ValueError:
            continue


enter_number()

# Пишем функцию, которая попросит пользователя ввести слово (строка без пробелов в
# середине, а вначале и в конце пробелы могут быть – их стоит удалить перед проверкой).
# Пока он не введёт правильно, просите его ввести. Функция возвращает введённое слово.


def enter_string():
    while True:
        word = input("Enter a word: ")
        word = word.strip()
        # check space in the middle
        if ' ' in word:
            continue
        else:
            print(word)
            return word
            break


enter_string()


# Функция принимает три числа a, b, c. Функция должна определить, существует ли
# треугольник с такими сторонами и если существует, то возвращает тип треугольника
# Equilateral triangle (равносторонний), Isosceles triangle (равнобедренный), Versatile triangle
# (разносторонний) или не треугольник (Not a triangle).


def triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        if a == b == c:
            return "Equilateral triangle"
        elif a == b or b == c or a == c:
            return "Isosceles triangle"
        else:
            return "Versatile triangle"
    else:
        return "Not a triangle"


print(triangle(5, 5, 4))
print(triangle(5, 5, 4))
print(triangle(7, 5, 8))
print(triangle(1, 1, 9))

# Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2,
# y2), вычисляющую расстояние между точками с координатами (x1, y1) и (x2, y2). Считайте
# четыре действительных числа от пользователя и выведите результат работы этой функции.

import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


x1 = float(input("Enter a value for x1: "))
x2 = float(input("Enter a value for x2: "))
y1 = float(input("Enter a value for y1: "))
y2 = float(input("Enter a value for y2: "))

print(distance(x1, x2, y1, y2))

# Напишите функцию, которая удаляет все небуквенные символы внутри строки
# (ограничимся латинским алфавитом).


def remove_symbols():
    letters = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    phrase = input("Enter a phrase: ")
    for ch in phrase:
        if ch not in letters:
            phrase = phrase.replace(ch, "")
    return phrase


print(remove_symbols())









