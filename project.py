# Simple Cash register 
#Collecting user membership information
print("Memberships are Gold, Silver, Bronze and Free")
membership = input("What membership do you have? ")
membership = membership.lower()
#Stating if membership was selected or not
memberships = ("gold","silver","bronze","free")
if membership not in memberships:
    print("No membership selected")
else:
    print("Membership selected is",membership)
    #Items available at the store for user to buy
    items = ["APPLE","CALCULATOR","CHOCOLATE","ICE CREAM","CHICKEN"]
    for item in items:
                print(item)
    print("Choose from the list above")
        #if user enters invalid product code will not run
    product = input("What are you buying? ")
    product = product.upper()
    if product in items:
        print("Product selected is",product)
        price = float(input("How much does it cost? "))      
        if membership == "gold":
            totalgold = price - price/5 
            print("You have a 20% discount")
            print(f"That'll be £{totalgold:.2f}")

        elif membership == "silver":
            totalsilver = price - price/10
            print("You have a 10% discount")
            print(f"That'll be £{totalsilver:.2f}")

        elif membership == "bronze":
            totalbronze = price - price/20
            print("You have a 5% discount")
            print(f"That'll be £{totalbronze:.2f}")

        else:
            print("You have No discount")
            print(f"That'll be £{price:.2f}")
    else:#asking user to re-input product 
            chance2 = input("Choose a correct item from the list above ")
            chance2 = chance2.upper()
            if chance2 not in items:
                print("Invalid product entered")
            else:
                print("Product selected is",product)
                price = float(input("How much does it cost? "))      
                if membership == "gold":
                        totalgold = price - price/5 
                        print("You have a 20% discount")
                        print(f"That'll be £{totalgold:.2f}")

                elif membership == "silver":
                        totalsilver = price - price/10
                        print("You have a 10% discount")
                        print(f"That'll be £{totalsilver:.2f}")

                elif membership == "bronze":
                        totalbronze = price - price/20
                        print("You have a 5% discount")
                        print(f"That'll be £{totalbronze:.2f}")

                else:
                        print("You have No discount")
                        print(f"That'll be £{price:.2f}")
            
chance = input("Type yes to try again ")
chance = chance.lower()
#asking user to re-input their membership
if chance == "yes":
    membership2 = input("Select a valid membership: gold, silver, bronze or free ")
    membership2 = membership2.lower()
    if membership2 in memberships:
        print("Membership selected is",membership2)
    #Items available at the store for user to buy
        items = ["APPLE","CALCULATOR","CHOCOLATE","ICE CREAM","CHICKEN"]
        for item in items:
                print(item)
        print("Choose from the list above")
            #if user enters invalid product code will not run
        product = input("What are you buying? ")
        product = product.upper()
        if product in items:
            print("Product selected is",product)
            price = float(input("How much does it cost? "))      
            if membership2 == "gold":
                    totalgold = price - price/5 
                    print("You have a 20% discount")
                    print(f"That'll be £{totalgold:.2f}")

            elif membership2 == "silver":
                    totalsilver = price - price/10
                    print("You have a 10% discount")
                    print(f"That'll be £{totalsilver:.2f}")

            elif membership2 == "bronze":
                    totalbronze = price - price/20
                    print("You have a 5% discount")
                    print(f"That'll be £{totalbronze:.2f}")

            else:
                    print("You have No discount")
                    print(f"That'll be £{price:.2f}")
        else:#asking user to re-input product
            chance2 = input("Choose a correct item from the list above ")
            chance2 = chance2.upper()
            if chance2 not in items:
                print("Invalid product entered")
            else:
                print("Product selected is",product)
                price = float(input("How much does it cost? "))      
                if membership2 == "gold":
                        totalgold = price - price/5 
                        print("You have a 20% discount")
                        print(f"That'll be £{totalgold:.2f}")

                elif membership2 == "silver":
                        totalsilver = price - price/10
                        print("You have a 10% discount")
                        print(f"That'll be £{totalsilver:.2f}")

                elif membership2 == "bronze":
                        totalbronze = price - price/20
                        print("You have a 5% discount")
                        print(f"That'll be £{totalbronze:.2f}")

                else:
                        print("You have No discount")
                        print(f"That'll be £{price:.2f}")
    else:#if membership still wrong code will restart
        print("Try again")
else:#if chance is not yes code will restart
    print("Try again")