#This is a simple Python script that demonstrates the use of variables, type casting, and conditional if/elif/else statements using logical operators. It defines several variables related to a subscription eligibility checker, takes user input for identity verification, age, and ID possession, and then prints out a summary of the eligibility based on the user's input.

print("Subscription Eligibility Checker!")
print()

verified = bool(input("Enter your signature to verify your identity: "))
print()

if not verified:
    print("Identity verification failed. Access denied.")
else:
    print("Identity verified. Access granted.")
    print()

    age = int(input("Enter your age: "))
    has_id = bool(input("Do you have a valid ID? (Yes/No): ").strip().upper() == "YES")
    print()
    
    if (age < 18) or (not has_id):
        print("You are not eligible for the subscription. Either you are under 18 or you do not have a valid ID.")
    else:
        print("You are eligible for the subscription!")