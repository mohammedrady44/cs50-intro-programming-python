import re

def main():
    print(convert(input("Hours: ")))


def convert(st):
    matching = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$",st)
    
    if not matching or (int(matching.group(1)) > 12 or int(matching.group(4)) > 12):
        raise ValueError
    
    th,fo = check(matching.group(2)),check(matching.group(5))
    f,s = int(matching.group(1)),int(matching.group(4))
    f,s = calculate(f,matching.group(3)),calculate(s,matching.group(6))
    return f"{f:02}:{th:02} to {s:02}:{fo:02}"

def check(n):
    if n:
        if int(n) > 59:
            raise ValueError
        else:
            return int(n)
    return 0            

def calculate(t,u):
    if u == "PM" and t != 12:
       return t + 12
    return t




if __name__ == "__main__":
    main()