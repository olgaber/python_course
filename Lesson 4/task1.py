# Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не
# является числом (любым), то должна выполняться конкатенация, т. е. соединение, строк. В
# остальных случаях введённые числа суммируются.

value1 = input("Enter the first value: ")
value2 = input("Enter the second value: ")
try:
    value1 = float(value1)
    value2 = float(value2)
    print(value1 + value2)
except ValueError:
    print(value1 + value2)



