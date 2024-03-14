def get_breads(breads, flour_stock):
    available_breads = []
    sorted_breads = sorted(breads, key=lambda x: x["flour"])
    for bread in sorted_breads:
        if flour_stock >= bread["flour"]:
            available_breads.append(bread["name"])
            flour_stock -= bread["flour"]
        else:
            break
    return available_breads

bread1 = [
    {"name": "donut", "flour": 25},
    {"name": "mini puff", "flour": 15},
    {"name": "baguette", "flour": 75},
    {"name": "cupcake", "flour": 15},
]

bread2 = [
  {"name": "pancake", "flour": 15},
  {"name": "waffle", "flour": 25},
  {"name": "bagel", "flour": 15},
  {"name": "cupcake", "flour": 15},
  {"name": "choco chips", "flour": 10},
  {"name": "mini puff", "flour": 5},
  {"name": "bread", "flour": 30},
]

print(get_breads(bread1, 100))
print(get_breads(bread2, 75))