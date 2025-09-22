import validators

emai = input("What's your email address? ")
matching = validators.email(emai)
if matching:
    print("Valid")
else:
    print("Invalid")    
