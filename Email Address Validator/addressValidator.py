def addressVal(address):
    dot = address.find(".")
    at = address.find("@")
    if (dot == -1):
        print("Invalid address, 'dot' missing ")
    elif (at == -1):
        print("Invalid address, '@' missing ")
    else:
        print("Valid email address")
        print("------------------------")
        
while(True):
    print("---Email Validator---")
    print("A valid email address needs an '@' symbol and a '.'")
    x = input("Input your email address: ")

    addressVal(x)