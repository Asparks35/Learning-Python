import math
print("Welcome to Capstone investment and Bond calculator")

print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")

while True:
    choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ") 
    choice = choice.lower()#to prevent any unnecessary errors
    choices = ("investment", "bond")
    if choice in choices:
        break
    else:
        print("Choose either 'Investment' or 'Bond'")
if choice == "investment":
    while True:#if user input is false it will continue to loop through until true
        principal = input("How much money are you depositing? ")        
        rate = input("What is the interest rate?(Do not include the % sign) ")    
        time = input("How long do you plan on investing? ")
        try:
            principal = float(principal)
            rate = float(rate)/100
            time = int(time)
        except:#to catch value error
            print("One of the values filled out above is not a numerical values ")
        else:
            break
        while True:
            interest = input('Would you like "Simple" or "Compound" interest for this investment?(Only write the words in quotation marks) ')
            interest = interest.lower()#to prevent any unnecessary errors

            if interest == "simple":
                    simple  = total = principal *(1 + rate*time)#calculations for simple interest
                    print(f"You will have £{total:.2f} at the end of {time}years using simple interest")
                    break

            elif interest == "compound":
                while True:
                    compound =  total = principal * math.pow((1+rate),time)#calculations for compound interest
                    print(f"You will have £{total:.2f} at the end of {time}years using compound interest")
                    break
if choice == "bond":
    while True:
        Present_value = input("What is the present value of your house? ")
        interest_rate = input("What is the interest rate? ")
        num_of_months = input("What is the number of months you plan to take to repay the bond? ")
        try:
            Present_value = float(Present_value)
            interest_rate = float(interest_rate)/100
            num_of_months = int(num_of_months)
        except:
            print("One of the filled values above is not numerical")
            continue
        repayment = (interest_rate * Present_value)/(1 - (1 + interest_rate)**(-num_of_months))
        print(f"You'll need £{repayment:.2f} over a period of {num_of_months}months" )
        break

                

            
                    
                
        