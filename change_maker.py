import math
quarters = 25
dimes = 25
nickels = 25
ones = 0
fives = 0
dollars = ((quarters * .25) + (dimes * .10) + (nickels *.05))
check = True

print ("Welcome to the vending machine change maker program")
print ("Change maker initialized.")

while check==True:
    cancel = True
    runs = True
    print("Stock contains:")
    print(f'   {int(nickels)} nickels')
    print(f'   {int(dimes)} dimes')
    print(f'   {int(quarters)} quarters')
    print(f'   {int(ones)} ones')
    print(f'   {int(fives)} fives')
    print()

    purchase_price = input("Enter the purchase price (xx.xx) or `q' to quit:")
    if purchase_price == 'q':
        total = int((quarters*.25 + dimes*.10 + nickels*.05)*100)
        print()
        print(f'Total: {int(total//100)} dollars and {int(total%100)} cents')
        check = False
        runs = False
        cancel = False
        break
        
    purchase_price = float(purchase_price)
    
    while runs==True:
        purchase_price = float(purchase_price*100)
        if purchase_price % 5 == 0 and purchase_price >= 0:
            runs = False
        else: 
            print ("Illegal price: Must be a non-negative multiple of 5 cents.")
            print()
            purchase_price = float (input(("Enter the purchase price (xx.xx) or `q' to quit:")))
    print()
    print ("Menu for deposits:")
    print ("  'n' - deposit a nickel") 
    print ("  'd' - deposit a dime") 
    print ("  'q' - deposit a quarter") 
    print ("  'o' - deposit a one dollar bill")
    print ("  'f' - deposit a five dollar bill")
    print ("  'c' - cancel the purchase")
    print()

    if purchase_price // 100 == 0:
        print (f'Payment due: {int(purchase_price%100)} cents')
    else:
        print (f'Payment due: {int(purchase_price//100)} dollars and {int(purchase_price%100)} cents')
    deposit = input("Indicate your deposit:")
    change = []
    cancel = True
    while purchase_price > 0:
        if deposit == 'c': 
            print()
            print ('Please take the change below.')
            change_return = math.fabs(purchase_price)
            if  change_return // 25 > 0:
                num_of_coins = change_return//25
                quarters = quarters - (num_of_coins)
                if quarters >=0:
                    print(f'   {int(num_of_coins)} quarters')
                    change_return -= (num_of_coins*25)
            
            if change_return // 10 > 0:
                num_of_coins = change_return//10
                dimes = dimes - num_of_coins
                if dimes >= 0:
                    print(f'   {int(num_of_coins)} dimes')
                    change_return -= (num_of_coins*10)
                    
                else:
                    continue
            if change_return // 5 > 0:
                num_of_coins = change_return//5
                nickels -= num_of_coins
                if nickels>= 0:
                    print(f'   {int(num_of_coins)} nickels')
                    change_return -= (num_of_coins*5)
                else: 
                    continue
            cancel = False
            break
        elif deposit == 'n':
            purchase_price = (purchase_price - 5)
            change.append (5)
            nickels += 1
            if purchase_price < 0:
                break
            if purchase_price // 100 == 0:
                print (f'Payment due: {int(purchase_price%100)} cents')
                deposit = input("Indicate your deposit:")
            else:
                print (f'Payment due: {int(purchase_price//100)} dollars and {int(purchase_price%100)} cents')
                deposit = input("Indicate your deposit:")
        elif deposit == 'd':
            purchase_price = (purchase_price - 10)
            change.append (10)
            dimes += 1
            if purchase_price < 0:
                break
            if purchase_price // 100 == 0:
                print (f'Payment due: {int(purchase_price%100)} cents')
                deposit = input("Indicate your deposit:")
            else:
                print (f'Payment due: {int(purchase_price//100)} dollars and {int(purchase_price%100)} cents')
                deposit = input("Indicate your deposit:")
        elif deposit == 'q':
            purchase_price = (purchase_price - 25)
            change.append (25)
            quarters +=1
            if purchase_price < 0:
                break
            if purchase_price // 100 == 0:
                print (f'Payment due: {int(purchase_price%100)} cents')
                deposit = input("Indicate your deposit:")
            else:
                print (f'Payment due: {int(purchase_price//100)} dollars and {int(purchase_price%100)} cents')
                deposit = input("Indicate your deposit:")
        elif deposit == 'o':
            purchase_price = (purchase_price - 100)
            change.append (100)
            ones += 1
            if purchase_price < 0:
                break
            if purchase_price // 100 == 0:
                print (f'Payment due: {int(purchase_price%100)} cents')
                deposit = input("Indicate your deposit:")
            else:
                print (f'Payment due: {int(purchase_price//100)} dollars and {int(purchase_price%100)} cents')
                deposit = input("Indicate your deposit:")
        elif deposit == 'f':
            purchase_price = (purchase_price - 500)
            change.append (500)
            fives += 1
            if purchase_price < 0:
                break
            if purchase_price // 100 == 0:
                print (f'Payment due: {int(purchase_price%100)} cents')
                deposit = input("Indicate your deposit:")
            else:
                print (f'Payment due: {int(purchase_price//100)} dollars and {int(purchase_price%100)} cents')
                deposit = input("Indicate your deposit:")
        else:
            print ("Illegal selection:", deposit)
            if purchase_price // 100 == 0:
                print (f'Payment due: {int(purchase_price%100)} cents')
                deposit = input("Indicate your deposit:")
            else:
                print (f'Payment due: {int(purchase_price//100)} dollars and {int(purchase_price%100)} cents')
                deposit = input("Indicate your deposit:")
        
    change_return = math.fabs(purchase_price)
    while cancel == True:
        if change_return > 0:
            print()
            print ("Please take the change below.")
            if  change_return // 25 > 0:
                num_of_coins = change_return//25
                quarters = quarters - (num_of_coins)
                if quarters >=0:
                    print(f'{int(num_of_coins)} quarters')
                    change_return -= (num_of_coins*25)
                    quarters -= num_of_coins
                else:
                    quarters += num_of_coins
            if change_return // 10 > 0:
                num_of_coins = change_return//10
                dimes = dimes - num_of_coins
                if dimes >= 0:
                    print(f'{int(num_of_coins)} dimes')
                    change_return -= (num_of_coins*10)
                    dimes -= num_of_coins
                else:
                    dimes+=num_of_coins
            if change_return // 5 > 0:
                num_of_coins = change_return//5
                nickels -= num_of_coins
                if nickels>= 0:
                    print(f'{int(num_of_coins)} nickels')
                    change_return -= (num_of_coins*5)
                    nickels -= num_of_coins
                else:
                    nickels += num_of_coins
                
            if change_return >0:
                print('Machine is out of change.')
                print('See store manager for remaining refund.')
                print(f'Amount due: {int(change_return)} cents')
                break
        else:
            cancel = False
    print()