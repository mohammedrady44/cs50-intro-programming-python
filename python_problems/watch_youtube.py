import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
  matching = re.search(r'src="(https?://(?:www\.)?youtube\.com/embed/xvFZjo5PgG0)"',s)
  if matching:
    return re.sub(r"https?://(?:www\.)?youtube\.com/embed","https://youtu.be",matching.group(1))
    
  else:
    return matching 




if __name__ == "__main__":
    main()