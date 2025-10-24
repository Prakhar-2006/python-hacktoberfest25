import random

number = random.randint(1, 100)
attempts = 0

print("🎯 Guess the Number (between 1 and 100)")

while True:
    guess = input("Enter your guess (or 'q' to quit): ")
    if guess.lower() == 'q':
        print("Game exited. The number was:", number)
        break

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
