def calculate_total(price, tax_rate=8):
    tax_amount = price * tax_rate / 100
    total_amount = price + tax_amount
    return tax_amount, total_amount

price = float(input("Enter price: "))

# Call 1: using the default tax rate (don't pass tax_rate at all)
default_tax, default_total = calculate_total(price)
print(f"Default tax rate — Tax: {default_tax}, Total: {default_total}")

# Call 2: overriding with a custom tax rate
custom_tax, custom_total = calculate_total(price, 12)
print(f"Custom tax rate (12%) — Tax: {custom_tax}, Total: {custom_total}")