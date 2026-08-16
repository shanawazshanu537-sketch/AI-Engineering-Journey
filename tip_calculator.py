def calculate_tip(bill_amount, tip_percent):
    tip = bill_amount * (tip_percent/100)
    return tip

bill_amount = float(input("Enter bill amount: "))
tip_percent = float(input("Enter tip percent: "))

tip_amount = calculate_tip(bill_amount, tip_percent)
total = bill_amount + tip_amount

print(f"Tip is {tip_amount} and total bill is {total}")
