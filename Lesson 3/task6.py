"""Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести
одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа"""

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a == b and b == c and a == c:
    print(3)

elif a == b or a == c or b == c:
    print(2)

else:
    print(0)