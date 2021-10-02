"""Создайте строку, в которой написан, какой-то текст.
Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
"""

s = "Daimler's decision to split, a huge, overwhelming hedge on the S&P 500! and back-and-forth over US infrastructure."
words = s.split(" ")
print(len(words))
print(words)

"""Удалите знаки препинания в списке слов (пройдитесь циклом все слова и удалите
методом strip знаки препинания)"""
for i in range(0, len(words)):
    words[i] = words[i].strip(" ,.! ")

print(words)

"""Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)"""
words.sort()
print(words)
