"""Дано три числа. Упорядочите их в порядке возрастания. Программа должна считывать три
числа a, b, c, затем программа должна менять их значения так, чтобы стали выполнены
условия a <= b <= c, затем программа выводит тройку a, b, c.
Дополнительные ограничения: нельзя использовать дополнительные переменные."""

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b:
    a, b = b, a

if b > c:
    b, c = c, b

if a > b:
    a, b = b, a

print(a, b, c)

