import random
import string

confusing = "O0l1I"

lowercase = "".join(c for c in string.ascii_lowercase if c not in confusing)
uppercase = "".join(c for c in string.ascii_uppercase if c not in confusing)
digits = "".join(c for c in string.digits if c not in confusing)
symbols = string.punctuation


lowUp = lowercase + uppercase
lowUpDig = lowUp + digits
lowUpDigSym = lowUpDig + symbols
password = ""

while True:
    print("🔐 Welcome to the Password Generator!")
    
    passLen = int(input("Enter the length of password: "))
    
    try:
        mode = int(input("Select the mode:\n1. Easy\n2. Medium\n3. Strong \nMake Your Selection: "))
    except ValueError:
        print("⚠️ Invalid input. Please enter a number.")
        continue
    try:
        qty = int(input("Enter the quantity of passwords: "))
    except ValueError:
        print("⚠️ Invalid input. Please enter a number.")
        continue

    if mode == 1:
        stren = lowUp
    elif mode == 2:
        stren = lowUpDig
    elif mode == 3:
        stren = lowUpDigSym
    else:
        print("⚠️ Invalid mode. Defaulting to Easy.")
        stren = lowUp

    for _ in range(qty):

        password = "".join(random.choice(stren) for _ in range(passLen))
        print(f"✅ Your password is: {password}")

    if input("Would you like to quit? (y/n): ").lower() == "y":
        break

