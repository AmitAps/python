from transactions import * #By importing the transactions module like this, you can call the functions without the module name.
import promotion
#You need to use this kind of import for “promotion.py” and “starbuzz.py”, because you are going to qualify the function names with the module names.
import starbuzz


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
        price = promotion.discount(prices[choice - 1]) #Code will call the "discount()" function.
        if input("Starbuzz card? ") == "Y":
            price = starbuzz.discount(price) #Id someone has a starbuzz discount card you need to apply the second starbuzz discount.
        save_transaction(price, credit_card, items[choice -1])
                            #"price" is the discount value of the price.
