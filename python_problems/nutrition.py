fruit  = input("Item: ")

calories = {
 "Apple":130,
 "Avocado":50,
 "Banana":110,
 "Cantaloupe":50,
 "Grapefruit":60,
 "Honeydew melon":50,
 "Lemon":15,
 "Nectarine":60,
 "Peach":60,
 "pear":100 ,
 "Orange":80,
 "Pineapple":50,
 "Strawberries":50,
 "Sweet Cherries":100,
 "Tangerine":50,
 "Watermelon":80,
 "Plums":70,
 "lime":20,
 "Nectarine":60
}

for key in calories:
    if key.lower() == fruit.lower():
        print(f"Calories: {calories[key]}")
        break


