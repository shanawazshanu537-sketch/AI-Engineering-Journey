weight = float(input("weight of a baggage: "))

if 0 <= weight <= 15:
    print("free")
elif 15.01 <= weight <= 23:
    print(f"$30 fee")
elif 23.01 <= weight <= 32:
    print(f"$75 fee")
elif weight >= 32:
    print("Not allowed - exceeds limit")