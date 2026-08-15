correct_pin = "4321"
attempts = 0
entered_pin = ""

while entered_pin != correct_pin and attempts < 3:
    entered_pin = input("Enter PIN: ")
    attempts += 1

if entered_pin == correct_pin:
    amount = int(input("Enter amount to withdraw (or 0 to exit): "))

    while amount != 0:
        print(f"Withdrawing {amount}")
        amount = int(input("Enter amount to withdraw (or 0 to exit): "))

    print("Thank you, goodbye!")
else:
    print("Card locked")