while True:
    first,second = input("Fraction: ").split("/")
    try:
        first,second = int(first),int(second)
        if first > second:
            continue
        percentage = round((first / second)*100)
        break
    except:
        pass 

if percentage >= 99:
    print("F")
elif percentage <= 1:
    print("E")
else:
    print(f"{percentage}%")                    

