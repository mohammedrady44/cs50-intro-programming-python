import re

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    matching = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$",ip)
    if not matching:
        return False
    f,s,t,fo = matching.group(1),matching.group(2),matching.group(3),matching.group(4)
    
    if int(f) < 256 and int(s) < 256 and  int(t) < 256 and int(fo) < 256:
        return True
    else:
        return False

    


if __name__ == "__main__":
    main()