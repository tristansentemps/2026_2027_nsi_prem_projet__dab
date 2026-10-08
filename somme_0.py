import random
argent = random.randint(-5000,10000)
code = 1234
def verify_pin():
    if code==1234:
        print(f"You have ${argent} on your bank account")
    else:
        print("Incorrect PIN")
    return(code) 