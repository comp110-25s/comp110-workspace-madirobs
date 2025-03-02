"""Wordle Exercise for COMP 110"""

__author__ = "730673399"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    max_turns = 6
    turns_taken = 0
    won = False
    while turns_taken < max_turns and not won:
        turns_taken += 1
        print(f"===Turn {turns_taken}/{max_turns} ===")
        guess = input_guess(len(secret))
        if guess == secret:
            won = True
            result = f"You won in {turns_taken}/{max_turns} turns!"
        else:
            result = emojified(guess, secret)
            print(result)
    if won:
        print(f"You won in {turns_taken}/{max_turns} turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


def contains_char(all_char: str, single_char: str) -> bool:
    """Code to find if a character guessed is in the secret word"""
    assert len(single_char) == 1, f"len('{single_char}') is not 1"
    index = 0
    while index < len(all_char):
        if all_char[index] == single_char:
            return True
        index += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Returns string of emojis to show correctness of wordle guess"""
    assert len(guess) == len(secret), "Guess must be the same length as secret"
    result = ""
    i = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1
    return result


def input_guess(expected_length: int) -> str:
    """Given guess is the correct number of characters as the expected length"""
    guess = input(f"Enter a {expected_length} character word:")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again:")
    return guess


if __name__ == "__main__":
    """Makes the program fully run."""
    main(secret="codes")
