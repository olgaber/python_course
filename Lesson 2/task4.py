d = {"title": "",
        "price": 120.25,
        "ingredients": ['cheese', 'tomato', 'sausages']}

# 1
d.update({"description": "description text"})
print(d)

# 2
d["price"] += 100
print(d["price"])

# 3
d["ingredients"].append("mushrooms")
print(d["ingredients"])

# 4
print(len(d["ingredients"]))

# 5
d.pop("description")
print(d)