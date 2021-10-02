phrase = "Why Are There Two Jokers in a Deck of Cards?"
#1
ls = phrase.split(" ")
print(ls[-3])

#2
print(ls[1][0])

#3
print(ls[-1][-1])

#4
ls.append("world")
print(ls)

#5
ls.insert(3, "new")
print(ls)

#6
print(ls)

#7
ls.remove("world")
print(ls)
