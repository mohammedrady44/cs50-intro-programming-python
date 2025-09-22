goods = {}
while True:
    try:
        item = input().upper()
        if item in goods:
            goods[item] += 1
        else:
            goods[item] = 1
    except EOFError:
        break            

for key in sorted(goods):
    print(f"{goods[key]} {key}")