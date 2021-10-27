# Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:
# 1-е число – сколько строк будет в песне. По умолчанию 3
# 2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
# 3-е число – если 0, то в конце песни (в конце последней строчки) стоит точка, если 1, то в конце
# стоит «!». По умолчанию 0

def generate_song(lines_number=3, la_number=3, symbol=0):
    line = 'la' * la_number + '\n'
    song = line * lines_number
    if symbol == 0:
        song = song.rstrip() + '.'
    if symbol == 1:
        song = song.rstrip() + '!'

    print(song)


generate_song()
generate_song(3, 4, 0)
generate_song(3, 4, 1)

