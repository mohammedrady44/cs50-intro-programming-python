#without using regular expression 

import re
import sys

f = input("Text: ").lower()
def main():
    print(count())

def count():
    size = len(f)
    if size < 2:
        return 0
    
    count,start,end = 0,0,2
    while end <= size:
        if check(f[start:end],start - 1,end):
            count += 1
            start = end
            end += 2
        else:
            start += 1
            end += 1
    return count            
             
     
def check(t,previous,next):
    if t != "um":
        return False
    
    if previous != -1:
        if not sub_check(previous):
            return False
    
    if next < len(f):
        if not sub_check(next):
            return False

    return True    


def sub_check(num):
    if (f[num] >= "a" and f[num] <= "z") or (f[num] >= "0" and f[num] <= "9") or (f[num == "_"]):
        return False
    return True


if __name__ == "__main__":
    main()