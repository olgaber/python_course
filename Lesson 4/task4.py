# Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов
# (неопределенное количество). Учитываем, что может быть повторяющиеся значения аргументов.

def second_min(*args):
    ls = [*args]
    min_el = min(ls)
    print(min_el)

    #print full list of arguments
    print(ls)

    ls.remove(min_el)

    #print list of arguments without min value
    print(ls)

    #check and remove other appearances of min value
    for value in ls:
        if value == min_el:
            ls.remove(value)

    #print final arguments list
    print(ls)

    #find second min value
    new_min_el = min(ls)
    print(new_min_el)


second_min(0, 5, 3, 0, 24, 145, 0)
