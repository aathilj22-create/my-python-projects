import random

secret_number = random.randint(1, 100)

print("I have thought of a number between 1 and 100. Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number!")
        break
    elif guess > secret_number:
        print("Too High! Try a smaller number.")
    else:
        print("Too Low! Try a bigger number.")
input("\nPress Enter to exit...")