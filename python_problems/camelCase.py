camel = input("camelCase:  ")
snake = ""
for letter in camel:
    if letter == letter.upper():
        snake += "_"
        snake += letter.lower()
    else:
        snake += letter
print(f"snake_case: {snake}")             