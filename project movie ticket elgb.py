age = int(input("Enter your age: "))
answer = input("Do you have a parent with you? (yes/no): ")
has_parent = answer == "yes"

is_eligible = age >= 18 or (age >= 13 and has_parent)
print(f"Are you eligible? {is_eligible}")
