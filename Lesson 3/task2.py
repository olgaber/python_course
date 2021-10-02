"""Пользователь вводит строку. Разрежьте её на две части – равные, если длина строки чётная, а
если длина строки нечётная, то длина первой части должна быть на один символ больше.
Переставьте эти две части местами, результат запишите в новую строку и выведите на экран."""

s = input("Enter a string: ")

if len(s) % 2 == 0:
    first_half = s[0:(int(len(s)/2))]
    second_half = s[int(len(s)/2):]
else:
    first_half = s[0:(int(len(s) / 2) + 1)]
    second_half = s[int(len(s) / 2) + 1:]

s_reversed = second_half + first_half
print(s_reversed)