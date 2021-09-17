#1
a = 367
b = 127
c = a**2 + b**2

print("c = " + str(c))

#2
d = 87

print(d//10)

#3
e = 777

hundreds = e//100
tens = (e - hundreds*100)//10
ones = e % 10

print(hundreds + tens + ones)

#4
n = 18

if (n % 2 == 0):
    print(n + 2)
else:
    print(n + 1)

#5
x = 682.53
ls = str(x).split(".")
print(ls[1])

#6
y = 54645.4454
ls = str(y).split(".")
print(ls[1][0])

