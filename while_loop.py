correct_pin = 231005
attempt = 3

while attempt>0:
    pin = int(input("Enter Your ATM PIN:"))

    if pin == correct_pin:
        print("Access Successful!")
    else:
        print("Access failed")
        attempt -= 1
        print("attemt remaining:", attempt)

if attempt == 0:
    print("ATM CARD BLOCKED FOR 24 HOURS")
    


