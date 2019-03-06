def save_transaction(price, credit_card, description):
    file = open("transactions.txt", "a") #The "a" means you are alays going to APPEND records to the end of the file.
    file.write("%s%07d%s\n" % (credit_card, price * 100, description))
                    #This is the format for string you just created.
    file.close()

items = ["DOUNT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.50, 2.0, 1.80, 1.20]
running = True

while running: #The loop will keep running while the "running" variable has the value True. To end the loop,set "running" to False.
    option = 1
    for choice in items:
        print(str(option)+ ". " + choice)
        option = option + 1
    print(str(option) + ". Quit")
    choice = int(input("Choose an option: ")) #The user inters a menu option number to make a sale.
    if choice == option: #This will be True if the user selects the LAST option on the menu, which is "Quit".
        running = False
    else:
        credit_card = input("Credit card number: ")
        save_transaction(prices[choice -1], credit_card, items[choice -1])
