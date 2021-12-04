"""
1) Создайте список 2 в степени N, где N от 0 до 20.
"""
res = [2**N for N in range(0, 21)]
print(res)

"""2) У вас есть список целых чисел. Создайте новый список остатков от деления на 3 чисел из
исходного списка."""

initial_list = [n for n in range(1, 21)]
# new list
res = [k % 3 for k in initial_list]
print(res)
# new dictionary
diction = dict(list(zip(initial_list, res)))
print(str(diction))

"""
3) У вас есть список, в котором могут быть разные типы данных. Создайте новый список
только чисел из этого списка.
"""

initial_list = [1, "cbvbcb", 456, {"2": "1", "70": "jhjjhjj"}, 212154, [1, 2, 5, 8]]
res = [n for n in initial_list if isinstance(n, int)]
print(res)

"""4) У вас есть список, в котором могут быть разные типы данных. Создайте новый список
только строк, при этом удалите усе небуквенные символы из них. Воспользуйтесь
функцией из предыдущего задания (импортируйте её из другого своего файла)"""


def remove_extra(s):
    new_str = "".join([ch for ch in s if ch.isalpha()])
    return new_str


initial_list = [1, "cbvbc345!*&*&^b", 456, {"2": "1", "70": "jhjjhjj"}, 212154, [1, 2, 5, 8], "!@##$234456456dsfbsnf"]
res = [remove_extra(s) for s in initial_list if isinstance(s, str)]
print(res)

"""
5) У вас есть словарь – характеристик человека. Ключи, например,: “name”, “surname”, “age”,
“position”, “address”, “skills”.
- Сгенерируйте новый словарь с такими же ключами, а в значениях типы значений.
- Сгенерируйте новый словарь с только парами ключ-значение, если значение исходного
словаря было строкой. 
Значения нового словаря должны быть переведены в нижний
регистр и удалены всё небуквенные символы из них.
"""

initial_dict = {
    "name": "Paul",
    "surname": "James",
    "age": 30,
    "position": "QA",
    "address": "Paul's address",
    "skills": {
        "English": "Upper Intermediate",
        "German": "Basic"
    }
}

d1 = {k: type(v) for k, v in initial_dict.items()}
print(d1)

d2 = {k: v.lower() for k, v in initial_dict.items() if type(v) == str}
print(d2)