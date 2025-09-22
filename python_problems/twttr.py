def main():
    text = input("Input: ")
    print( shorten(text))

def shorten(text):
    n_text = ""
    vowels = ["a","i","e","o","u"]
    for letter in text:
        if letter.lower() not in vowels:
            n_text += letter
    return f"Output: {n_text}"

if __name__ == "__main__":
    main()