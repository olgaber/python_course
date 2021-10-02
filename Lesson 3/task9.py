"""Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
если год високосный, и False иначе."""


def is_year_leap(yr):
    if yr % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


s = input("Enter a year: ")
year = int(s)

print(is_year_leap(year))

"""Функция принимает три числа a, b, c. Функция должна определить, существует ли
треугольник с такими сторонами. Если треугольник существует, вернёт True, иначе False."""


def is_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False


x = int(input("Enter the first side length: "))
y = int(input("Enter the second side length: "))
z = int(input("Enter the third side length: "))

print(is_triangle(x, y, z))