vip_count = 0 

for number in range(1,11):
    if number % 3 == 0:
        print(f"ticket {number}: VIP")
        vip_count +=1
    else:
        print(f"ticket {number}: standard")


print(f"Total VIP tickets: {vip_count}")