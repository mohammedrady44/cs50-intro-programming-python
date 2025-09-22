from basicfunc import my_strip
value = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()
possible = ["42","forty two","forty-two"]
if my_strip(value) in possible:
    print("Yes")
else:
    print("No")    

