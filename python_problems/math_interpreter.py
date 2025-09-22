expre = input("Expression: ").split()
if expre[1] == "+":
    result = float(expre[0]) + float(expre[2])
elif expre[1] == "-":
    result = float(expre[0]) - float(expre[2])
elif expre[1] == "*":
    result = float(expre[0]) * float(expre[2])
elif expre[1] == "/":
    result = float(expre[0]) / float(expre[2])
print(f"{result:.1f}")                        