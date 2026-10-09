# This is a simple Python script that demonstrates the use of variables, type casting, user input, boolean values, and conditional if/elif/else statements using logical operators. It defines several variables related to a restaurant reservation system, takes user input for holiday reservations, number of seats, reservation details, and special occasions, and then calculates the reservation fee based on reservation conditions before printing out a summary of the reservation if it is confirmed.

print("Restaurant Reservation System!")
print()

reservation_fee = 0.00
holiday = input("Are you reserving during holiday season? (Yes/No): ").strip().upper() == "YES"
number_of_seats = int(input("How many seats do you want to reserve? (4-12): "))
print()

if 4 <= number_of_seats <= 12:
    print("Reservation Form. Please provide the reservation details.")
    name = input("Name: ")
    contact_number = input("Contact Number: ")
    date_time_reservation = input("Date and Time: ")
    occasion = input("Occasion (optional, leave blank if none): ")
    has_occasion = bool(occasion)
    print()

    if holiday and has_occasion:
        reservation_fee = 100 * number_of_seats * 1.5
    elif holiday and (8 <= number_of_seats):
        reservation_fee = 50 * number_of_seats * 1.5
    elif holiday or (has_occasion and (8 <= number_of_seats)):
        reservation_fee = 25 * number_of_seats * 1.5
    elif has_occasion:
        reservation_fee = 20 * number_of_seats * 1.5
    else:
        reservation_fee = 20 * number_of_seats

    print(f"Reservation Fee: ₱{reservation_fee:.2f}")
    print()
    
    reserved = input("Confirm the reservation? (Yes/No): ").strip().upper() == "YES"
    print()
    
    if not has_occasion:
        occasion = "N/A"
    
    if reserved:
        print("Confirmed Reservation Details")
        print(f"Name: {name}")
        print(f"Contact Number: {contact_number}")
        print(f"Date and Time: {date_time_reservation}")
        print(f"Occasion: {occasion}")
        print(f"Reservation Fee: ₱{reservation_fee:.2f}")
        print()

        print("Thank you for your reservation! See you! :)")
    else:
        print("Not reserved. Sad to see you go. :(")
else:
    if number_of_seats < 4:
        print("Sorry, this reservation system only accepts reservations for 4 to 12 seats. For fewer than 4 seats, please consider walking in.")
    else:
        print("Sorry, this reservation system only accepts reservations for 4 to 12 seats. For groups larger than 12, please contact us directly.")