user_name = input("enter your name: ")
user_age = int(input("enter your age: "))
fvrt_hobby = input("enter your favorite hobby: ")
user_name = user_name.strip().title()
name_length = len(user_name)
age_in10y = user_age + 10

print("====================")
print("PERSONAL INFO CARD")
print("====================")

print(f"Name: {user_name}")
print(f"Age {user_age}")
print(f"in 10 years: {age_in10y}")
print(f"hobby: {fvrt_hobby}")
print(f"Name length: {name_length} characters ")

print("====================")
