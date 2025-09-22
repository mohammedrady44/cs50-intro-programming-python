def main():
    plate = input("Plate: ")
    size = len(plate)
    conditions = []
    conditions.append(size > 6 or size < 2)
    conditions.append(check_string(plate[0:2]) != -1)
    conditions.append((index := check_string(plate)) != -1 and plate[index] == "0")
    conditions.append(check_middle(plate) == False)
    for condition in conditions:
        if condition == True:
            print("Invalid")
            break
    else:
        print("Valid")    


def check_string(text):
    for i in range(0,len(text)):
        if text[i].lower() < "a" or text[i].lower() > "z":
            return i
    return -1


def check_middle(text):
    ready = False
    for letter in text: #check of the numbers at the end,also check the letter if it is number,letter
        if check_string(letter) != -1 and (letter < "0" or letter > "9"):
            return False    
        
        if letter >= "0" and letter <= "9":
            ready = True
        
        elif ready == True:
            return False
    return True    

main()        
        

    