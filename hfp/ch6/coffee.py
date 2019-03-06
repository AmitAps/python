from transactions import *

items = ["DOUNT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.50, 2.0, 1.80, 1.20]
running = True

while running: #The loop will keep running while the "running" variable has the value True. To end the loop,set "running" to False.
    option = 1
    for choice in items:
        print(str(option)+ ". " + choice)
        option = option + 1
    print(str(option) + ". Quit")
    choice = int(input("Choose an option: ")) #The user enters a menu option number to make a sale.
    if choice == option: #This will be True if the user selects the LAST option on the menu, which is "Quit".
        running = False
    else:
        credit_card = input("Credit card number: ")
        save_transaction(prices[choice -1], credit_card, items[choice -1])
