from basicfunc import get_int
import random
def main():
    while True:
        l  = get_int("Level: ")
        if l in [1,2,3]:
            break

    score = 0
    for _ in range(10):
        num_1 = generate_int(l)
        num_2 = generate_int(l)
        real = num_1 + num_2
        for i in range(3):
            try:
                answer =  int(input(f"{num_1} + {num_2} = "))
                if answer == real:
                    score += 1
                    break 
                else:
                    raise ValueError     

            except ValueError:
                print("EEE")
                if i == 2:
                    print(f"{num_1} + {num_2} = {real}")

    print(f"Score: {score}")               


def generate_int(l):
    if l == 1:
        n = random.randint(0,9)
    elif l == 2:
        n = random.randint(10,99)
    else:
        n = random.randint(100,999)
    return n        

main()

