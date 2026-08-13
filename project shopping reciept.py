item_name = input("enter a item name: ")
price = float(input("enter a price: "))
quantity = int(input("how much quantity: ")) 

item_name = item_name.strip().title()
name_length = len(item_name)

total = price * quantity
if quantity > 5:
    total = total * 0.9
else:
    total = total

print("===================")
print("Shopping receipt")
print("===================")

print(f"item name: {item_name}")
print(f"price: {price}")
print(f"quantity: {quantity}")
print(f"total after discount if applied: {total}")
print(f"name length: {name_length}")

print("===================")
