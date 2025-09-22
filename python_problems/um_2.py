#using regular expression 
import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
   matching = re.findall(r"\bum\b",s,re.IGNORECASE)
   return len(matching)



if __name__ == "__main__":
    main()