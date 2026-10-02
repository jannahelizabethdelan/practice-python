# This is a simple Python script that demonstrates the use of variables, type casting, and conditional if/elif/else statements. It defines several variables related to a squishy store transaction, takes user input for hourly wage, hours willing to work, and squishy price, and then prints out a summary of the transaction based on the user's budget and savings.

print("Welcome to Squishy Saver Store!")
print("Where you can buy squishy and save money at the same time!")
print()

hourly_wage = float(input("How much is your hourly wage?: $"))
willing_to_work_hours = float(input("How many hours are you willing to work to buy a squishy?: "))
print()

squishy_budget = hourly_wage * willing_to_work_hours * 0.30
squishy_savings = hourly_wage * willing_to_work_hours * 0.20

print(f"Your squishy budget is ${squishy_budget:.2f}.")
print(f"Your total savings is ${squishy_savings:.2f}.")
print()

print("Squishy Menu:")
print("$5.00 - Butter Squishy")
print("$2.50 - Dumpling Squishy")
print("$5.25 - Strawberry Squishy")
print("$9.75 - Big Cheese Squishy")
print("$14.00 - Crunchy Peanut Squishy")
print()

squishy_price = float(input("How much is the squishy you want to buy?: $"))
print()

if squishy_price < squishy_budget:
    squishy_budget = squishy_budget - squishy_price
        
    print("Congratulations! You can buy the squishy! Your change can go to your savings or you can try to buy another squishy!")
elif squishy_price == squishy_budget:
    squishy_budget = squishy_budget - squishy_price
    
    print("Congratulations! You can buy the squishy! You don't have any change left.")
elif squishy_price <= (squishy_budget + squishy_savings):
    squishy_savings = (squishy_savings + squishy_budget) - squishy_price
    squishy_budget = 0.00

    print("You can buy the squishy, but you used your savings to buy it. You don't have any change left.")
else:
    squishy_price = 0.00

    print("Sorry, you cannot afford this squishy. You need to work more hours to save up for it or choose a cheaper squishy.")
print()

print(f"You bought ${squishy_price:.2f} worth of squishy.")
print(f"Money left in squishy budget: ${squishy_budget:.2f}")
print(f"Money left in squishy savings: ${squishy_savings:.2f}")
print()

print("Thank you for visiting Squishy Saver Store! Have a squishy day!")