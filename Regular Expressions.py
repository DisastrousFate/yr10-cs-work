import re

def enterName():
    name = input("Enter your name: ")
    valid = re.match("[A-Z]",name)
    if valid:
        print("That looks OK")
    else:
        print("Invalid, no capital!")
        enterName()

def enterHometown():
    town = input("Enter your hometown: ")
    valid = re.match("[A-Z]",town)
    if valid:
        print("That looks OK")
    else:
        print("Invalid, no capital!")
        enterHometown()
	
def enterEmail():
    email = input("Enter your email address: ")
    valid = re.match("[a-z]",email)
    if valid:
        print("That looks OK")
    else:
        print("Erm, try again!")
        enterEmail()

def enterPhoneNumber():
    number = input("Enter your email address: ")
    valid = re.match("[0,9]",number)
    if valid:
        print("That looks OK")
    else:
        print("Erm, try again!")
        enterPhoneNumber()

def enterPostcode():
    code = input("Enter your postcode: ")

    def validFunc():
        validList = []
        validList.append(re.match("[A-Z][A-Z][0-9][0-9] [0-9][A-Z][A-Z]",code)) # TS16 1DA
        validList.append(re.match("[A-Z][A-Z][0-9] [0-9][A-Z][A-Z]",code)) # DT2 7EW
        validList.append(re.match("[A-Z][0-9] [0-9][A-Z][A-Z]",code)) # W1 8BL
        validList.append(re.match("[A-Z][0-9][0-9] [0-9][A-Z][A-Z]",code)) # C17 9DF

        for x in validList:
            if x:
                return x
    valid = validFunc()
    if valid:
        print("That looks OK")
    else:
        print("Erm, try again!")
        enterPostcode()

enterName()
enterHometown()
enterEmail()
enterPhoneNumber()

enterPostcode()
