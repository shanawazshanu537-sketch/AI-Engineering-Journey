user_num = int(input("enter a number: "))

is_even = user_num % 2 == 0 #here it checks remainder is equals to zero than automatic we know it is said to be even because even numbers ehen divided with zero remainds 0
is_greater_than100 = user_num > 100 #logic here print bool

print(f"is it even? {is_even}")
print(f"is it greater than 100? {is_greater_than100}")