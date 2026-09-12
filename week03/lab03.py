import random


def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
    return f"One day a {adjective} {noun} decided to {verb} through the park."


def guessing_game():
    """Run an interactive number-guessing game."""
    secret = random.randint(1, 100)

    while True:
        guess = int(input("Enter your guess: "))

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("Correct! You guessed it!")
            break
