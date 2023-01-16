customer = input("Enter your name: ")
totalamount = 0
while True:
    softdrink = int(input("Number of soft drinks: "))
    sandwich = int(input("Number of sandwich: "))
    sf = 17.00
    sw = 20.00
    totalamount = totalamount + softdrink * sf + sandwich * sw
    discount = totalamount * 0.15
    dc = totalamount - discount
    print("\nCustomer Name: ", customer)
    print("total bill: ", totalamount)
    print("Discount: ", discount)
    print("total bill (including discount): ", dc)
    repeat = input("\nbuy again? (yes/no): ")
    if repeat.lower() == "no":
        amount = float(input("Amount tendered: "))
        change = amount - dc
        print("Change: ", change)
        break
    else:
        continue