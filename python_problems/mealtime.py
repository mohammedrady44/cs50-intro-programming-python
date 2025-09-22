def main():
    value =  convert(input("What time is it? "))
    if value >= convert("7:00") and value <= convert("8:00"):
        print("breakfast time")
    elif value >= convert("12:00") and value <= convert("13:00"):
        print("lunch time")
    elif value >= convert("18:00") and value <= convert("19:00"):
        print("dinner time")
            
        
def convert(time):
    hour_12 = ""
    num = 0
    expression = time.split(" ")
    first,second = expression[0].split(":")
    first,second = float(first),float(second)
    if len(expression) == 2:
        hour_12 = expression[1]
        if hour_12 == "p.m." and first != 12:
            num = 12  
    first += num  
    final = first + (second / 60)
    return final


if __name__ == "__main__":
    main()