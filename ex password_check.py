correct_password = "python123"
attempts = 0
entered_password = ""

while entered_password != correct_password and attempts < 3:
    entered_password = input("password: ")
    attempts += 1

if entered_password == correct_password:
    print("access granted")
else:
    print("Account locked")
