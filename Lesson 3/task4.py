"""Даны три числа a, b, c. Определите, существует ли треугольник с такими сторонами. Если
треугольник существует, выведите строку YES, иначе выведите строку NO."""

a = int(input("Enter the first side length: "))
b = int(input("Enter the second side length: "))
c = int(input("Enter the third side length: "))

if a + b > c and b + c > a and a + c > b:
    print("YES")
else:
    print("NO")



