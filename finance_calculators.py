import math
print("Welcome to Capstone investment and Bond calculator")

print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")

choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ") 
choice = choice.lower()#to prevent any unnecessary errors
choices = ("investment", "bond")
if choice not in choices:
    print("Invalid choice")
if choice == "investment":
    principal = float(input("How much money are you depositing? "))
    rate = float(input("What is the interest rate? "))/100
    time = int(input("How long do you plan on investing? "))
    interest = input('Would you like "Simple" or "Compound" interest for this investment?(Only write the words in quotation marks) ')
    interest = interest.lower()#to prevent any unnecessary errors
    if interest == "simple":
        simple  = total = principal *(1 + rate*time)#calculations for simple interest
        print(f"You will have £{total:.2f} at the end of {time}years using simple interest")
            
    elif interest == "compound":
        compound =  total = principal * math.pow((1+rate),time)#calculations for compound interest
        print(f"You will have £{total:.2f} at the end of {time}years using compound interest")
    else:
        print("Choose a valid answer")

if choice == "bond":
    Present_value = float(input("What is the present value of your house? "))
    interest_rate = float(input("What is the interest rate? "))/100
    num_of_months = int(input("What is the number of months you plan to take to repay the bond? "))
    repayment = (interest_rate * Present_value)/(1 - (1 + interest_rate)**(-num_of_months))
    print(f"You'll need £{repayment:.2f} over a period of {num_of_months}months" )