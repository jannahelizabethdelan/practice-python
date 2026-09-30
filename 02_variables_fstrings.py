# This is a simple Python script that demonstrates the use of variables, type casting, and fstrings. It defines several variables related to a transaction at a store, takes user input for item name, quantity, tip, and verification, and then prints out a summary of the transaction.

print("Welcome to the Dollar Store!")
print("All items are $1.00 each!")
print()

item_name = input("Which item would you like to buy: ")
item_quantity_string = input(f"How many {item_name}s would you like to buy: ")
tip_string = input("How much would you like to tip for this transaction: ")
print()

print("[Warning!] Leaving this blank will result in an unverified transaction.")
verified_string = input("Verify the transaction by signing: ")
print()

item_quantity = int(item_quantity_string)
tip = float(tip_string)
verified = bool(verified_string)

print("Transaction Summary:")
print(f"{item_quantity}x {item_name}(s) @ $1.00 each . . . ${(1.00 * item_quantity):.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Total: ${((1.00 * item_quantity) + tip):.2f}")
print(f"Verified transaction?: {verified}")
