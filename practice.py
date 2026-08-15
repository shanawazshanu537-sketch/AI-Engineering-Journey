secret_number = 7
guess = ""
guess_counter = 0

while guess != secret_number:
    guess = int(input("guess that secret number: "))
    guess_counter += 1

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    elif guess == secret_number:
        print("Correct! You win")

print(f"guess counter: {guess_counter}")
        