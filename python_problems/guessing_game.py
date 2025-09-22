from random import randint
from basicfunc import get_int

def main():
    l = intial("Level: ")
    num = randint(1,l)
    while True:
        g = intial("Guess: ")
        if g == num:
            print("Just right!")
            break
        elif g < num:
            print("Too small!")
        else:
            print("Too large!")

def intial(t):
    while True:
        s = get_int(t)
        if s > 0:
            return s

main()